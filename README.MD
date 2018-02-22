# Sorting Material Design Icons

### Current directory tree:
```
material-design-icons
|
+--category (e.g action)
   |
   +--screen pixel density (e.g drawable-mdpi)
      |
      +--icon (e.g ic_3d_rotation_black_18dp.png)
```

This makes it difficult to locate and copy each icon especially if you need all different pixel densities.

### What I propose:
```
material-design-icons
|
+--category (e.g action)
   |
   +--icon name (e.g ic_3d_rotation_black_18dp.png)
      |
      +--icon pixel density(.e.g 18dp)
         |
         +--screen pixel density (e.g drawable-mdpi)
            |
            +icon (e.g ic_3d_rotation_black_18dp.png)
```

It makes it easier to locate icons

### How to use:

```
$ ./sort-icons.py /path/to/icons
```

You will find the icons in ```sorted``` folder in ```/path/to/icons/```

### Official Material design icons repo:
Clone the repo from [github.com/google/material-design-icons](https://github.com/google/material-design-icons)

## Contributing

Bug reports and pull requests are welcome on GitHub at [github.com/robincheptileh/material-design-icons-sort](https://github.com/RobinCheptileh/material-design-icons-sort). This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The project is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

## Code of Conduct

Everyone interacting in the material-design-icons-sort project’s codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/RobinCheptileh/material-design-icons-sort/blob/master/CODE_OF_CONDUCT.md).
