# Life Progress

This is a script for generating life expectancy progress bars. 
It was used in this blog post: http://www.usrsb.in/memento-mori.html.

## Requirements

Python >= 3.5 with the following additional packages is required:

* [click](http://click.pocoo.org)

## Usage

```
Usage: life-progress.py [OPTIONS] BIRTHDAY

Options:
  --books INTEGER   Books per month
  --coffee INTEGER  Cups of coffee per month
  --male            Defaults to female
  --help            Show this message and exit.
```

# Credits

The concept is from [Scott Hendrickson](https://blog.drskippy.net/2012/11/11/age-visualization/),
who in turn was inspired by Sha Hwang.

## License

Licensed unter the terms of the MIT license. Please refer to [LICENSE](LICENSE).
