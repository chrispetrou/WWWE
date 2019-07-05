<img src="images/1.png" width="25%">
<img src="images/2.png" width="30%">

##### A tool to help you check if your email(s) have appeared in a data-breach!
[![GPLv3 license](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://github.com/chrispetrou/WWWE/blob/master/LICENSE) 
[![](https://img.shields.io/badge/python-3-yellow.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/) 
[![Build Status](https://travis-ci.org/chrispetrou/WWWE.svg?branch=master)](https://travis-ci.org/chrispetrou/WWWE) 
![version](https://img.shields.io/badge/version-1.1-lightgray.svg) 
[![Known Vulnerabilities](https://snyk.io//test/github/chrispetrou/WWWE/badge.svg?targetFile=requirements.txt)](https://snyk.io//test/github/chrispetrou/WWWE?targetFile=requirements.txt)
* * *

`WWWE.py` is a standalone python script that checks an email or a list of emails using popular online services to see it the email(s) appear on any security-breach happened in the past. The online services used are:

- [x] [__Google search engine__](https://www.google.com/)
- [x] [__HaveIBeenPwned__](https://haveibeenpwned.com)
- [x] [__HaveIBeenSold__](https://haveibeensold.app)
- [x] [__inoitsu__](https://www.hotsheet.com/inoitsu/)
- [x] [__LEAKEDSOURCE__](https://leakedsource.ru/)
- [x] [**hack_check**](https://www.avast.com/hackcheck/friends-check/)
- [x] [__DEHASHED__](https://www.dehashed.com)

```
$ python WWWE.py -h
usage: WWWE.py [-h] (-e  | -f ) [--timeout]

WWWE.py: What's Wrong With my Email.

optional arguments:
  -h, --help     show this help message and exit
  -e , --email   Specify an email to check.
  -f , --file    Specify a file that contains a list of emails.
  --timeout      Specify HTTP connection timeout [default 10 sec]
```

### Example

<img src="images/example.png" width="80%">

### Requirements - Installation:

> This project requires the following being installed on your system:

*   python-requirements
*   geckodriver
*   PhantomJS
*   Firefox

You can install the first three __automatically__ using the `setup.sh` script (_for the time only Linux/Mac OS are supported_) or __manually__ as follows:

To install the _python-requirements_ :

`pip install -r requirements.txt --upgrade --user`

But you also need to install:
*   [__Firefox__](https://www.mozilla.org/en-US/firefox/new/)
*   [__PhantomJS__](http://phantomjs.org/)
*   [__Mozilla GeckoDriver__](https://github.com/mozilla/geckodriver/releases)

### TODO
- [ ] Add the ability to save the results in csv format (_work in progress_).
- [ ] Provide results in a __json__ format also, so the results be _easily_ used and accessed by other tools.

### Contributions & Feedback

Feedback and contributions are welcome. If you find any bug or have a feature request feel free to open an issue, and as soon as I review it I'll try to fix it!

### Disclaimer
>This tools is only for testing and academic purposes and can only be used where strict consent has been given. Do not use it for illegal purposes! It is the end user’s responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this software.

## Credits

*   Logo designed with [fontmeme.com](https://fontmeme.com/graffiti-fonts/)!

## License

This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details