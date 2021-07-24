# Life Progress

This is a script for generating life expectancy progress bars. 
It was used in this blog post: http://www.usrsb.in/memento-mori.html.

## Requirements

Python 3.8 or greater.

## Usage

```
$ python life-progress.py -h
usage: life-progress.py [-h] [--books BOOKS] [--coffee COFFEE] [--female] birthday

positional arguments:
  birthday         YYYY-MM-DD

optional arguments:
  -h, --help       show this help message and exit
  --books BOOKS    Books per month
  --coffee COFFEE  Cups of coffee per month
  --female         Calculate with actuarial tables for females

```

Example: `python3 life-progress.py --books 1 --coffee 60 1988-10-03`

```
 0 ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 

10 ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 

20 ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 

30 ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
   ■ ■ ■ ■ ■ ■ ■ ■ ■ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   0.986, Books: 87, Cups of Coffee: 5220
40 □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   0.956, Books: 207, Cups of Coffee: 12420
50 □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   0.885, Books: 327, Cups of Coffee: 19620
60 □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   0.755, Books: 447, Cups of Coffee: 26820
70 □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   0.522, Books: 567, Cups of Coffee: 34020
80 □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □  Life expectancy
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   0.186, Books: 687, Cups of Coffee: 41220
90 □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   □ □ □ □ □ □ □ □ □ □ □ □ 
   0.010, Books: 807, Cups of Coffee: 48420
```

# Credits

The concept is from [Scott Hendrickson](https://blog.drskippy.net/2012/11/11/age-visualization/),
who in turn was inspired by Sha Hwang.

## License

Licensed under the terms of the [MIT License](LICENSE).
