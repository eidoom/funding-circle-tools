# Funding Circle tools

Tested on Fedora 31.

## Dependancies

* Pandas `sudo dnf install python3-pandas`
* matplotlib `sudo dnf install python3-matplotlib`
* wordcloud `pip install --user wordcloud`

## Usage

* `./income-forecase.py CSV_FILE` graphs income forecast from [`My Portfolio > My Loan Parts > Dwnload repayment schedule`](https://www.fundingcircle.com/investors/portfolio)
* `./all-loan.py CSV_FILE` shows various statistics about loans from [`My Portfolio > My Loan Parts > Download all loans`](https://www.fundingcircle.com/investors/portfolio)

## `old`

* These are the legacy tools, which no longer work on the current website
