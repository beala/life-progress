# -*- coding: utf-8 -*-

import argparse
import math
import sys
from datetime import datetime
from typing import List


# p_survive_to(0, 1) calculates the probability that you'll survive to your 1st birthday assuming you've just
# been born.
def p_survive_to(p_die_in_one_year: List[float], cur_age: int, age: int) -> float:
    if age <= cur_age:
        return 1.0
    else:
        # P(survive to your n-1th birthday) * P(survive to your nth birthday | you've just had your n-1th birthday)
        # There is only one thing we say to death: Not today.
        return p_survive_to(p_die_in_one_year, cur_age, age - 1) * (1 - p_die_in_one_year[age - 1])


def is_decade(year: int) -> bool:
    return year % 10 == 0


def years_to_months(years: int, months: int = 0) -> int:
    return years * 12 + months


def render(p_die_in_one_year: List[float],
           render_to_year: int,
           age_months: int,
           books_per_month: int,
           coffee_per_month: int):
    age_years = int(math.floor(age_months / 12))

    for year in range(0, render_to_year):
        # Draw decade annotation
        if is_decade(year):
            sys.stdout.write('\n')
            sys.stdout.write('{:2d} '.format(year))
        else:
            sys.stdout.write('   ')

        # Draw boxes
        for month in range(0, 12):
            if 12 * year + month < age_months:
                sys.stdout.write('■ ')
            else:
                sys.stdout.write('□ ')

        # Draw life expectancy marker. From https://www.ssa.gov/cgi-bin/longevity.cgi
        if year == 82:
            sys.stdout.write(' Life expectancy')

        sys.stdout.write('\n')

        # Draw probability, coffee, and books annotation if the *next* year is a decade.
        next_year = year + 1
        if is_decade(next_year) and next_year > age_years:
            annotation_string = '   {:.3f}'.format(
                p_survive_to(p_die_in_one_year, age_years, year + 1)
            )
            if books_per_month > 0:
                books_read = (years_to_months(year, months=12) - age_months) * books_per_month
                annotation_string += ', Books: {}'.format(books_read)
            if coffee_per_month > 0:
                coffees_drank = (years_to_months(year, months=12) - age_months) * coffee_per_month
                annotation_string += ', Cups of Coffee: {}'.format(coffees_drank)
            sys.stdout.write(annotation_string)

    print('\n')
    sys.stdout.flush()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('birthday', help="YYYY-MM-DD")
    parser.add_argument('--books', type=int, default=0, help='Books per month')
    parser.add_argument('--coffee', type=int, default=0, help='Cups of coffee per month')
    parser.add_argument('--female', action='store_true', help='Calculate with actuarial tables for females')
    args = parser.parse_args()

    parsed_birthday = datetime.fromisoformat(args.birthday)
    now = datetime.now()
    age_months = ((now.year - parsed_birthday.year) * 12) + (now.month - parsed_birthday.month)

    render_to_year = 100

    # Each entry in p_die_in_one_year is the probability of surviving a certain age, given that you've just turned
    # that age. So, p_die_in_one_year[0] is the probability you'll survive your first year of life, given that you've
    # just been born. Data comes from this table: https://www.ssa.gov/oact/STATS/table4c6.html
    p_die_in_one_year = []
    death_prob_per_year_file = './death-prob-men.tsv' if not args.female else './death-prob-women.tsv'
    with open(death_prob_per_year_file, 'r') as death_probability_raw:
        for death_prob_per_year in death_probability_raw:
            p_die_in_one_year.append(float(death_prob_per_year))

    render(p_die_in_one_year, render_to_year, age_months, args.books, args.coffee)


if __name__ == '__main__':
    main()
