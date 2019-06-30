<img src="images/logo.png" width="80%">

#### WWWE: What's Wrong With my Email? </br> A tool to help you check if your email(s) have appeared in a data-breach!
[![GPLv3 license](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://github.com/chrispetrou/WWWE/blob/master/LICENSE) [![](https://img.shields.io/badge/Made%20with%20python-3-lightgreen.svg)](https://www.python.org/) ![version](https://img.shields.io/badge/version-1.0-lightgray.svg)
* * *

`WWWE.py` is a standalone python script that checks an email or a list of emails using popular online services to see it the email(s) appear on any security-breach happened in the past. The online services used are:

- [x] [HaveIBeenPwned](https://haveibeenpwned.com)
- [x] [HaveIBeenSold](https://haveibeensold.app)
- [x] [inoitsu](https://www.hotsheet.com/inoitsu/)
- [x] [LEAKEDSOURCE](https://leakedsource.ru/)
- [x] [hack check](https://www.avast.com/hackcheck/friends-check/)
- [x] [DEHASHED](https://www.dehashed.com)

```
python WWWE.py -h
usage: WWWE.py [-h] (-e  | -f )

WWWE.py: What's Wrong With my Email.

optional arguments:
  -h, --help     show this help message and exit
  -e , --email   Specify an email to check.
  -f , --file    Specify a file that contains a list of emails.
```

### Requirements:

To install the _python-requirements_ :

`pip install -r requirements.txt --upgrade --user`

But you also need to install:
*   [__Firefox__](https://www.mozilla.org/en-US/firefox/new/)
*   [__PhantomJS__](http://phantomjs.org/)
*   [__Mozilla GeckoDriver__](https://github.com/mozilla/geckodriver/releases)

### TODO
- [ ] Add the ability to save the results in csv format (_work in progress_).

### Contributions & Feedback

Feedback and contributions are welcome. If you find any bug or have a feature request feel free to open an issue, and as soon as I review it I'll try to fix it!

### Disclaimer
>This tools is only for testing and academic purposes and can only be used where strict consent has been given. Do not use it for illegal purposes! It is the end user’s responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this software.

## Credits

*   Logo designed with [fontmeme.com](https://fontmeme.com/graffiti-fonts/)!

## License

This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details