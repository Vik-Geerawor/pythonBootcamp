def problem2():
    # http://www.pythonchallenge.com/pc/def/map.html
    text =\
        'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc ' + \
        'dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr ' + \
        'gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

    print(text)

    text2 = text.replace('k', 'm').replace('o', 'q').replace('e', 'g')

    print(f"{text2}")


if __name__ == '__main__':
    print("\n*** pythonchallenge.com ***")
    problem2()
