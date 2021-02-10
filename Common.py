
# coding: utf-8

# In[ ]:


# 한글처리
def visualKoSetting():
    import platform
    import matplotlib.pyplot as plt
    from matplotlib import font_manager, rc
    plt.rcParams['axes.unicode_minus'] = False

    osName = platform.system()
    if osName == 'Darwin': # 맥
        rc('font', family='AppleGothic')
    elif osName == 'Windows': # 윈도우
        path = 'c:/Windows/Fonts/malgun.ttf'
        font_name = font_manager.FontProperties(fname=path).get_name()
        print( font_name )
        rc('font', family=font_name)
    else:# 기타 os(리눅스..)
        pass

    
# 한글 세팅 사용
visualKoSetting()

