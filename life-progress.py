# -*- coding: utf-8 -*-
import sys
import math

age_months = (29 * 12) + 5
male = False
coffee_per_month = 30
books_per_month = 1
render_to_year = 90

age_years = int(math.floor(age_months / 12))

# Each entry in p_die_in_one_year is the probability of dying at a certain age, given that you've just turned that age.
# So, p_die_in_one_year[0] is the probability you'll survive your first year of life, given that you've just been
# born
# Data comes from this table: https://www.ssa.gov/oact/STATS/table4c6.html
p_die_in_one_year = []
death_prob_per_year_file = './death-prob-men.tsv' if male else './death-prob-women.tsv'
with open(death_prob_per_year_file, 'r') as death_probability_raw:
    for death_prob_per_year in death_probability_raw:
        p_die_in_one_year.append(float(death_prob_per_year))


# p_survive_to(0, 1) calculates the probability that you'll survive to your 1st birthday assuming you've just
# been born.
def p_survive_to(cur_age, age):
    if age <= cur_age:
        return 1.0
    else:
        # P(survive to your n-1th birthday) * P(survive to your nth birthday | you've just had your n-1th birthday)
        # There is only one thing we say to death: Not today.
        return p_survive_to(cur_age, age - 1) * (1 - p_die_in_one_year[age - 1])


def is_decade(year):
    return year % 10 == 0


def years_to_months(years, months=0):
    return years*12 + months


for year in range(0, render_to_year):

    # Draw decade annotation
    if is_decade(year):
        sys.stdout.write('\n')
        sys.stdout.write("%2d " % year)
    else:
        sys.stdout.write("   ")

    # Draw boxes
    for month in range(0, 12):
        if 12 * year + month <= age_months:
            sys.stdout.write('■ ')
        else:
            sys.stdout.write('□ ')

    # Draw life expectancy marker. From https://www.ssa.gov/cgi-bin/longevity.cgi
    if year == 82:
        sys.stdout.write(' Life expectancy')

    sys.stdout.write('\n')

    # Draw probability, coffee, and books annotation if the *next* year is a decade.
    next_year = year+1
    if is_decade(next_year) and next_year > age_years:
        books_read = years_to_months(year, month) - age_months * books_per_month
        coffees_drank = (years_to_months(year, month) - age_months) * coffee_per_month
        sys.stdout.write("   %.3f, Books: %d, Cups of Coffee: %d" %
            (p_survive_to(age_years, year+1),
            books_read,
            coffees_drank))

sys.stdout.flush()
