if __name__ == '__main__':
    pycon = {2016: "Portland", 2018: "Cleveland"}
    print(pycon)
    europython = {2017: "Rimini", 2018: "Edinburgh", 2019: "Basel"}
    print(europython)
    print()

    merged = pycon.copy()
    merged.update(europython)
    # print((merged := pycon.copy()).update(europython))
    print(merged)

    print(pycon | europython)

    merged2 = pycon.copy()
    merged2 |= europython
    print(merged2)

    print({**pycon, **europython})

    merged3 = pycon.copy()
    merged3 |= [(2017, "Rimini")]
    merged3 |= [(2018, "Edinburgh")]
    merged3 |= [(2019, "Basel")]
    print(merged3)

    pycon.update(europython)
    print(pycon)
