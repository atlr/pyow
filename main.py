# usage
#
#   PC | PSN | XBL
#   KR | US | EU
#


PSN ='PSN'
XBL ='XBL'
PC ='PC'
CONSOLES =[PSN, XBL]
PLATFORMS =[PSN, XBL, PC]

KR ='KR'
EU ='EU'
US ='US'
REGIONS =[KR, EU, US]

# gen_url( USER, PLATFORM )
#
#   USER of formats
#
#       NAME
#       NAME-NUM
#       NAME#NUM
#
#   PLATFORM of forms
#
#       PSN
#       XBL
#       PC REGION
#
#   REGION of forms
#
#       KR
#       US
#       EU
#
ERR_TOO_LONG_PLATFORM_ARG ='gen_url(_, platform_arg) tuple length greater than 2'
ERR_NONPLATFORM ='gen_url(_, platform_arg) not in {0})'.format(PLATFORMS)
ERR_NO_REGION ='gen_url(_, PC) given without region'
ERR_NONREGION ='gen_url(_, (_, REGION)) is not in {0}'.format(REGIONS)
def gen_url(name, platform_arg):

    BASE_URL ='https://playoverwatch.com/en-us/career/{0}'
    CONSOLE_URL_APPENDAGE ='{0}/{1}'
    PC_URL_APPENDAGE ='pc/{0}/{1}-{2}'

    platform =platform_arg
    region =None
    if isinstance(platform_arg, tuple):
        if len(platform_arg) >2:
            raise ValueError(ERR_TOO_LONG_PLATFORM_ARG)
        platform, region =platform_arg

    if platform not in PLATFORMS:
        raise ValueError(ERR_NONPLATFORM)

    if platform in CONSOLES:
        console =platform.lower()
        if '#' in name:
            name, _ =name.split('#')
        if '-' in name:
            name, _ =name.split('-')
        url =BASE_URL.format(CONSOLE_URL_APPENDAGE.format(console, name))
        return url

    elif PC ==platform:
        if not region:
            raise ValueError(ERR_NO_REGION)
        if region not in REGIONS:
            raise ValueError(ERR_NONREGION)
