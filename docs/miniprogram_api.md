### 热门游戏

``` json
https://iot.universal-space.cn//api/mns/mnsGameStatis/hotGameList?pageNo=1&pageSize=3

{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "pageNo": 1,
    "pageSize": 3,
    "totalPage": 1,
    "totalSize": 3,
    "data": [
        {
            "statisPage": "/pages/wacca/wacca-statis",
            "productModel": "D-017",
            "productImage": "https://static.universal-space.cn/images/20210225/1614238244-057dcd8807a598746053dfd049b76eeeW9kj2iIfL3P6in4TmlMMzqhnH1mQwN5p.jpg",
            "productId": 3160,
            "highestUser": "远哥制造",
            "highestScore": 1000000,
            "rank": 1,
            "recordPage": "/pages/wacca/wacca-detail",
            "totalCount": 1001418,
            "productName": "华卡音舞",
            "hightestUserAvatar": "https://thirdwx.qlogo.cn/mmopen/vi_32/F5cBVYtv8xn9OibEFKPkrdqaLSjdic6zwKLG2RLBVXB4to8lWtg5TuIH4X3jvqLnyFRg2NKiausFM1Eu07mhGdRVg/132"
        },
        {
            "statisPage": "/pages/record/music5-statis",
            "productModel": "D-016",
            "productImage": "https://static.universal-space.cn/images/20191031/1572486310-25604fd52c30a0c46ddc134883aab05c91PaG2FVp3bRLAqngHigilMJgiyksTtd.png",
            "productId": 3084,
            "highestUser": "寧々寧々寧",
            "highestScore": 10000000,
            "rank": 2,
            "recordPage": "/pages/record/music5-detail",
            "totalCount": 463296,
            "productName": "音律炫动5",
            "hightestUserAvatar": "https://thirdwx.qlogo.cn/mmopen/vi_32/jwGOeRZ97OGOFTpW8AsJJE0mSEbV5XqHeLQqR6GxAbYxGVPaC2gjwSjd5ItZDSBrdtWp06IavjpfMctsgrj2qA/132"
        },
        {
            "statisPage": "/pages/record/dance-statis",
            "productModel": "D-014",
            "productImage": "https://static.universal-space.cn/images/20191031/1572486333-6dcefe90e71e5d8af5e70e34990b5756xdLBciszqPoxQdhSkY040Qv4qBnIGjXC.png",
            "productId": 3071,
            "highestUser": "数字",
            "highestScore": 100000,
            "rank": 3,
            "recordPage": "/pages/record/dance-detail",
            "totalCount": 320442,
            "productName": "舞律炫步",
            "hightestUserAvatar": "https://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83eq4A3DNxnrhfjmnLXnPDCrhreuYrgHHDGZ4hEibjpwibfr4vQfcVLMPH7K9h32odHhOS8Pvy3IHBTYA/132"
        }
    ]
}
```

``` json
https://iot.universal-space.cn//api/mns/mnsGameStatis/myHotGameList?pageNo=1&pageSize=3

{
	"code": 1,
	"message": "success",
	"detail": "success",
	"retCode": 0,
	"retMsg": "success",
	"pageNo": 1,
	"pageSize": 3,
	"totalPage": 1,
	"totalSize": 3,
	"data": [{
		"statisPage": "/pages/wacca/wacca-statis",
		"productModel": "D-017",
		"productImage": "https://static.universal-space.cn/images/20210225/1614238244-057dcd8807a598746053dfd049b76eeeW9kj2iIfL3P6in4TmlMMzqhnH1mQwN5p.jpg",
		"productId": 3160,
		"rank": 1.0,
		"productTypeName": "音乐类",
		"recordPage": "/pages/wacca/wacca-detail",
		"totalCount": 1019583,
		"unLock": 1,
		"productName": "华卡音舞"
	}, {
		"statisPage": "/pages/record/music5-statis",
		"productModel": "D-016",
		"productImage": "https://static.universal-space.cn/images/20191031/1572486310-25604fd52c30a0c46ddc134883aab05c91PaG2FVp3bRLAqngHigilMJgiyksTtd.png",
		"productId": 3084,
		"rank": 2.0,
		"productTypeName": "音乐类",
		"recordPage": "/pages/record/music5-detail",
		"totalCount": 494467,
		"unLock": 1,
		"productName": "音律炫动5"
	}, {
		"statisPage": "/wacca2/wacca2-statis",
		"productModel": "D-018",
		"productImage": "https://static.universal-space.cn/images/20210401/1617239738-ee1ba88327a47ae94c9d34f8755d0a630JQj2tpXuQV1YQ1V2K9UyVVyUTyf7TvI.png",
		"productId": 3183,
		"rank": 3.0,
		"productTypeName": "音乐类",
		"recordPage": "/wacca2/wacca2-detail",
		"totalCount": 448515,
		"unLock": 0,
		"productName": "华卡音舞Ver.2"
	}]
}
```

### 总游戏次数、解锁机型数

``` json
https://iot.universal-space.cn//api/mns/mnsGameStatis/getUserGameSummary?

{
	"code": 1,
	"message": "success",
	"detail": "success",
	"retCode": 0,
	"retMsg": "success",
	"data": {
		"totalCount": "471",
		"unlockCount": "2",
		"lastProductId": "3160",
		"lastProductName": "华卡音舞",
		"lastScore": "914667.00"
	}
}
```

### 我的战绩

``` json
https://iot.universal-space.cn//api/mns/mnsGameStatis/getUserRecordList?

{
	"code": 1,
	"message": "success",
	"detail": "success",
	"retCode": 0,
	"retMsg": "success",
	"pageNo": 1,
	"pageSize": 2,
	"totalPage": 1,
	"totalSize": 2,
	"data": [{
		"statisPage": "/pages/wacca/wacca-statis",
		"highestDate": "2021-07-08 19:16:25",
		"productImage": "https://static.universal-space.cn/images/20210225/1614238244-057dcd8807a598746053dfd049b76eeeW9kj2iIfL3P6in4TmlMMzqhnH1mQwN5p.jpg",
		"productId": 3160,
		"highestScore": 1000000.000,
		"recordPage": "/pages/wacca/wacca-detail",
		"productName": "华卡音舞"
	}, {
		"statisPage": "/pages/record/music5-statis",
		"highestDate": "2020-10-18 18:28:37",
		"productImage": "https://static.universal-space.cn/images/20191031/1572486310-25604fd52c30a0c46ddc134883aab05c91PaG2FVp3bRLAqngHigilMJgiyksTtd.png",
		"productId": 3084,
		"highestScore": 8698795.000,
		"recordPage": "/pages/record/music5-detail",
		"productName": "音律炫动5"
	}]
}
```

``` json 
https://iot.universal-space.cn//api/mns/mnsGameStatis/hotGameList?pageNo=1&pageSize=4

{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "pageNo": 1,
    "pageSize": 4,
    "totalPage": 1,
    "totalSize": 4,
    "data": [
        {
            "statisPage": "/pages/wacca/wacca-statis",
            "productModel": "D-017",
            "productImage": "https://static.universal-space.cn/images/20210225/1614238244-057dcd8807a598746053dfd049b76eeeW9kj2iIfL3P6in4TmlMMzqhnH1mQwN5p.jpg",
            "productId": 3160,
            "highestUser": "远哥制造",
            "highestScore": 1000000,
            "rank": 1,
            "recordPage": "/pages/wacca/wacca-detail",
            "totalCount": 1001418,
            "productName": "华卡音舞",
            "hightestUserAvatar": "https://thirdwx.qlogo.cn/mmopen/vi_32/F5cBVYtv8xn9OibEFKPkrdqaLSjdic6zwKLG2RLBVXB4to8lWtg5TuIH4X3jvqLnyFRg2NKiausFM1Eu07mhGdRVg/132"
        },
        {
            "statisPage": "/pages/record/music5-statis",
            "productModel": "D-016",
            "productImage": "https://static.universal-space.cn/images/20191031/1572486310-25604fd52c30a0c46ddc134883aab05c91PaG2FVp3bRLAqngHigilMJgiyksTtd.png",
            "productId": 3084,
            "highestUser": "寧々寧々寧",
            "highestScore": 10000000,
            "rank": 2,
            "recordPage": "/pages/record/music5-detail",
            "totalCount": 463296,
            "productName": "音律炫动5",
            "hightestUserAvatar": "https://thirdwx.qlogo.cn/mmopen/vi_32/jwGOeRZ97OGOFTpW8AsJJE0mSEbV5XqHeLQqR6GxAbYxGVPaC2gjwSjd5ItZDSBrdtWp06IavjpfMctsgrj2qA/132"
        },
        {
            "statisPage": "/pages/record/dance-statis",
            "productModel": "D-014",
            "productImage": "https://static.universal-space.cn/images/20191031/1572486333-6dcefe90e71e5d8af5e70e34990b5756xdLBciszqPoxQdhSkY040Qv4qBnIGjXC.png",
            "productId": 3071,
            "highestUser": "数字",
            "highestScore": 100000,
            "rank": 3,
            "recordPage": "/pages/record/dance-detail",
            "totalCount": 320442,
            "productName": "舞律炫步",
            "hightestUserAvatar": "https://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83eq4A3DNxnrhfjmnLXnPDCrhreuYrgHHDGZ4hEibjpwibfr4vQfcVLMPH7K9h32odHhOS8Pvy3IHBTYA/132"
        },
        {
            "statisPage": "/wacca2/wacca2-statis",
            "productModel": "D-018",
            "productImage": "https://static.universal-space.cn/images/20210401/1617239738-ee1ba88327a47ae94c9d34f8755d0a630JQj2tpXuQV1YQ1V2K9UyVVyUTyf7TvI.png",
            "productId": 3183,
            "highestUser": "WACCA 伍 ocean cat出口气呀",
            "highestScore": 1000000,
            "rank": 4,
            "recordPage": "/wacca2/wacca2-detail",
            "totalCount": 316447,
            "productName": "华卡音舞Ver.2",
            "hightestUserAvatar": "https://thirdwx.qlogo.cn/mmopen/vi_32/0YRSb7hiaGZcUsmm7ibIR16LqN0icbicq33MjTCXJibzHKPG8iaRtuGpFrsvCo6AoaibHAvWsHs0LtRle3lRJ6PneIWcQ/132"
        }
    ]
}
```

``` json
https://iot.universal-space.cn//api/mns/mnsGameStatis/getUserRecordStatis?productId=3160

{
	"code": 1,
	"message": "success",
	"detail": "success",
	"retCode": 0,
	"retMsg": "success",
	"data": {
		"statisPage": "/pages/wacca/wacca-statis",
		"productImage": "https://static.universal-space.cn/images/20210225/1614238244-057dcd8807a598746053dfd049b76eeeW9kj2iIfL3P6in4TmlMMzqhnH1mQwN5p.jpg",
		"productId": 3160,
		"highestScore": 1000000.000,
		"recordPage": "/pages/wacca/wacca-detail",
		"userRank": 500,
		"totalCount": 468,
		"productName": "华卡音舞",
		"averageScore": 946811.900
	}
}
```

### 华卡音舞

``` json
https://iot.universal-space.cn//api/marv/wacca/getMemberInfo?

{
	"code": 1,
	"message": "success",
	"detail": "success",
	"retCode": 0,
	"retMsg": "success",
	"data": {
		"memberType": 3, // VIP 会员
		"validDays": 87, // 有效期
		"vipCount": 69, // VIP 次数
		"userLevel": 43, // 玩家等级
		"userExp": 4225, // 玩家经验值
		"waccaPoint": 9999, // WP
		"ticketCount": 4, // EX Ticket
		"boostBadgeCount": 0, // Boost Badge
		"boostBadgeSCount": 0, // Boost Badge S
		"trophyCount": 27, // 获得奖杯
		"unlockCount": 59, // 歌曲解锁
		"titleCount": 32, // 我的成就
		"userName": "远哥制造",
		"userTitle": "坚持直到我觉得厌烦了", // 当前成就称号
		"iconUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/icon/102074.png",
		"iconName": "和服伊莉莎白", // 当前头像
		"iconRarity": 2,
		"memberFee": 2000
	}
}
```

``` json
https://iot.universal-space.cn//api/mns/mnsGameStatis/getUserGameSummary?

{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "data": {
        "totalCount": "471",
        "unlockCount": "2",
        "lastProductId": "3160",
        "lastProductName": "华卡音舞",
        "lastScore": "914667.00"
    }
}
```

``` json
https://iot.universal-space.cn//api/unis/stores/List?longitude=121.507396&latitude=38.898553&productId=3160&pageNo=1&pageSize=20 HTTP/1.1

{
    "data": [
        {
            "store_id": 4531,
            "store_mobile": "",
            "head_image": "https://static.universal-space.cn/images/20210719/1626657090-c6212e0fe130d360c8fd9efb4a975e62U9bESei9hMLVpp4FOhqlYAVwdJv9O4hg.png",
            "distance": 7165,
            "store_logo": "https://static.universal-space.cn/images/20210719/1626657087-c6212e0fe130d360c8fd9efb4a975e6219FrFjmwSRV6FZGEXtZ3ZwcQ896cXUcB.png",
            "store_name": "东方英雄（中央大道店）",
            "store_address": "沙河口区西安路103-9号中央大道旅游文化购物中心",
            "brand_name": "",
            "brand_id": 0
        },
        {
            "store_id": 4564,
            "store_mobile": "",
            "head_image": "https://static.universal-space.cn/images/20210719/1626656994-c6212e0fe130d360c8fd9efb4a975e62aUG3pcvybuOMHQPo8iXmS8MyJsYUwXCF.png",
            "distance": 90741,
            "store_logo": "https://static.universal-space.cn/images/20210719/1626656992-c6212e0fe130d360c8fd9efb4a975e62xPNXfDe9k5GqHyGh9t7JJQePYoqWH3Ji.png",
            "store_name": "东方英雄（万成广场店）",
            "store_address": "旺角区万成广场三楼东方英雄",
            "brand_name": "",
            "brand_id": 0
        },
        {
            "store_id": 4617,
            "store_mobile": "",
            "head_image": "https://static.universal-space.cn/images/20210719/1626656951-06172b0d500ba99f71811cf8f19bfd90TVljePMSOF1hB7qFcDxOQSB2Lpo93aCb.png",
            "distance": 211198,
            "store_logo": "https://static.universal-space.cn/images/20210719/1626656949-06172b0d500ba99f71811cf8f19bfd907hPKIGeVl9SbVeF5ehZpYQtN9n8NdNQF.png",
            "store_name": "再现狂潮电玩城",
            "store_address": "S251(秦青路)首钢赛车谷",
            "brand_name": "",
            "brand_id": 0
        },
        {
            "store_id": 4624,
            "store_mobile": "",
            "head_image": "https://static.universal-space.cn/images/20210719/1626683874-c6212e0fe130d360c8fd9efb4a975e62YOmkMqqt4kIcHaIWnppwIp7ylYTmLTSr.png",
            "distance": 252421,
            "store_logo": "https://static.universal-space.cn/images/20210719/1626683871-c6212e0fe130d360c8fd9efb4a975e628LaaeoRooWd0KOLC4zKNHAcUlvRISMBg.png",
            "store_name": "东方英雄盘锦水游城店",
            "store_address": "步行街中兴路新玛特6层",
            "brand_name": "",
            "brand_id": 0
        },
        {
            "store_id": 3139,
            "store_mobile": "400-666-2303",
            "head_image": "https://static.universal-space.cn/images/20170516/1494900143-b914c32cd27ed3f7e40c97e393b1bda2LZ4T4tuyEc5Ez7As8QOYGbXk6RJybWCE.jpg",
            "distance": 277205,
            "store_logo": "https://static.universal-space.cn/images/20210719/1626657113-c6212e0fe130d360c8fd9efb4a975e62aIJQwSSgMuIYgSS7vd1ETK0sK8ZSuHvG.png",
            "store_name": "东方英雄（新玛特店）",
            "store_address": "大商新玛特六层",
            "brand_name": "",
            "brand_id": 0
        },
        {
            "store_id": 4561,
            "store_mobile": "",
            "head_image": "",
            "distance": 277313,
            "store_logo": "",
            "store_name": "四隆主题公园",
            "store_address": "东山街33号甲四隆广场4楼",
            "brand_name": "",
            "brand_id": 0
        },
        {
            "store_id": 4569,
            "store_mobile": "",
            "head_image": "https://static.universal-space.cn/images/20210719/1626656974-c6212e0fe130d360c8fd9efb4a975e62dVIit130UO2UXsZeGsabptSWt3IyCGmB.png",
            "distance": 282035,
            "store_logo": "https://static.universal-space.cn/images/20210719/1626656971-c6212e0fe130d360c8fd9efb4a975e62rZGyKXEsyG3e4Z81kvQ8HjuA2PU6Z1jl.png",
            "store_name": "东方英雄（大悦城店）",
            "store_address": "胜利北路320号（大悦城）",
            "brand_name": "",
            "brand_id": 0
        },
        {
            "store_id": 4033,
            "store_mobile": "",
            "head_image": "https://static.universal-space.cn/images/20201015/1602741969-815a70795a18a13f22f0643e2f435339hcpDm50KUk4Fhpos68bKIR3cunAss9ll.jpg",
            "distance": 357603,
            "store_logo": "https://static.universal-space.cn/images/20201015/1602741966-e26cd2a5bf096c746586c49b80497423P8AwCqQI6lkuM8AUmzyJI2gVM5YM7x3w.png",
            "store_name": "城市英雄天津津南吾悦广场店",
            "store_address": "新城吾悦广场三楼",
            "brand_name": "",
            "brand_id": 0
        },
        {
            "store_id": 3077,
            "store_mobile": "0432-68196633",
            "head_image": "https://static.universal-space.cn/images/20170516/1494923483-b914c32cd27ed3f7e40c97e393b1bda2xd51wyFn8Qec6ylQAtPNkadJy90lashx.jpg",
            "distance": 693402,
            "store_logo": "https://static.universal-space.cn/images/20210719/1626657172-c6212e0fe130d360c8fd9efb4a975e62wxq14XHWruDSPNe3wzv41lNPfdRdgf5H.png",
            "store_name": "东方英雄嘉年华",
            "store_address": "吉林大街财富广场5楼近万达影城",
            "brand_name": "",
            "brand_id": 0
        },
        {
            "store_id": 4541,
            "store_mobile": "",
            "head_image": "https://static.universal-space.cn/images/20201015/1602741557-ab93b77061968f1a4589f4cc680edb320D3Enk7lGICyufKJisqbrpt6hQbYkKeG.jpg",
            "distance": 867403,
            "store_logo": "https://static.universal-space.cn/images/20201015/1602741552-69bd0d73f1a315193467a6e7785e2a5btO7BIlmFmwDC9ReAvtuXkKEC3D4CIc7J.jpg",
            "store_name": "奇奇乐园仲盛世界城店",
            "store_address": "都市路5001仲盛世界城 L3",
            "brand_name": "",
            "brand_id": 0
        },
        {
            "store_id": 4593,
            "store_mobile": "",
            "head_image": "",
            "distance": 938569,
            "store_logo": "",
            "store_name": "爱玩星球（驻马店）",
            "store_address": "乐山路1096号爱克CBD玖隆茂购物中心三楼爱玩星球",
            "brand_name": "",
            "brand_id": 0
        },
        {
            "store_id": 4519,
            "store_mobile": "",
            "head_image": "https://static.universal-space.cn/images/20201015/1602741990-815a70795a18a13f22f0643e2f435339lg9LBKuk821RKJerzsV0qDbZ4zn7aIiY.jpg",
            "distance": 1075592,
            "store_logo": "https://static.universal-space.cn/images/20201015/1602741987-e26cd2a5bf096c746586c49b80497423oLxS68USwqlpEwGQtjxCgpuL3zuE66f7.png",
            "store_name": "城市英雄义乌吾悦店",
            "store_address": "浙江省义乌市江东东路与宾王路交叉口新城吾悦广场3006城市英雄",
            "brand_name": "",
            "brand_id": 0
        },
        {
            "store_id": 4049,
            "store_mobile": "",
            "head_image": "",
            "distance": 1134559,
            "store_logo": "",
            "store_name": "嗨森汇乐园(光谷店)",
            "store_address": "东湖高新技术开发区珞喻路726号世界城光谷步行街一期3楼",
            "brand_name": "",
            "brand_id": 0
        },
        {
            "store_id": 64,
            "store_mobile": "0717-6255819",
            "head_image": "https://static.universal-space.cn/images/20170210/1486708294-807426d1243009874d37c3c3f032a5bdtTU3zrjLZk5Jl7RucVgD705BaLSIiURp.jpg",
            "distance": 1296761,
            "store_logo": "https://static.universal-space.cn/images/20170210/1486708287-f3ccdd27d2000e3f9255a7e3e2c48800cTTOACDv5OIyCSLtNIuQlQHfHpo47Ax2.jpg",
            "store_name": "奇奇乐园宜昌店",
            "store_address": "夷陵路58号CBD中心购物广场3楼",
            "brand_name": "",
            "brand_id": 0
        },
        {
            "store_id": 4520,
            "store_mobile": "",
            "head_image": "https://static.universal-space.cn/images/20201015/1602741950-815a70795a18a13f22f0643e2f43533960Bt7fQOdIfeKXhnsXbrHEGbOSFIY0sQ.jpg",
            "distance": 1411738,
            "store_logo": "https://static.universal-space.cn/images/20201015/1602741946-e26cd2a5bf096c746586c49b80497423VpBDtlMu6vJoW3OWoPuwbmieVKr2EmsI.png",
            "store_name": "城市英雄星沙吾悦店",
            "store_address": "东四路与特立东路交汇处吾悦广场城市英雄星沙吾悦店",
            "brand_name": "",
            "brand_id": 0
        },
        {
            "store_id": 4592,
            "store_mobile": "",
            "head_image": "",
            "distance": 1419217,
            "store_logo": "",
            "store_name": "量子时空舱游艺中心",
            "store_address": "万家丽北路地铁5号线·水渡河站蟠龙时代广场3F",
            "brand_name": "",
            "brand_id": 0
        },
        {
            "store_id": 4576,
            "store_mobile": "",
            "head_image": "",
            "distance": 1421131,
            "store_logo": "",
            "store_name": "101电玩(万家丽店)",
            "store_address": "万家丽路99号万家丽国际购物广场8楼",
            "brand_name": "",
            "brand_id": 0
        },
        {
            "store_id": 4521,
            "store_mobile": "",
            "head_image": "https://static.universal-space.cn/images/20201015/1602741909-815a70795a18a13f22f0643e2f4353397nySCHxapehHIaa0La8ViqrhSH00YWNn.jpg",
            "distance": 1421704,
            "store_logo": "https://static.universal-space.cn/images/20201015/1602741905-e26cd2a5bf096c746586c49b804974235YQjOBkWRBKbIJbO7hZ4k5c7eGHaSkPh.png",
            "store_name": "城市英雄(奥克斯广场店)",
            "store_address": "银盆岭街道岳麓大道57号奥克斯广场3-01、3-02城市英雄",
            "brand_name": "",
            "brand_id": 0
        },
        {
            "store_id": 4614,
            "store_mobile": "",
            "head_image": "https://static.universal-space.cn/images/20210615/1623717557-965461bf497f14ad06cbcedc3b1e09a0l1kfQwma10P1IQBfVBl7czFJ2AYM91Je.jpg",
            "distance": 1422509,
            "store_logo": "https://static.universal-space.cn/images/20210615/1623717554-965461bf497f14ad06cbcedc3b1e09a0vKyftH2ABUSX2ecNMc0KTVn6CyrPHJSc.jpg",
            "store_name": "子洋联盟电玩城运达店",
            "store_address": "长沙大道567号运达汇负一层LG150A号",
            "brand_name": "",
            "brand_id": 0
        },
        {
            "store_id": 4597,
            "store_mobile": "",
            "head_image": "",
            "distance": 1815085,
            "store_logo": "",
            "store_name": "第一回合(成都银泰城店)",
            "store_address": "益州大道1999号银泰城B1层(永辉超市出口处)",
            "brand_name": "",
            "brand_id": 0
        }
    ],
    "length": 20,
    "pageNo": 1,
    "pageSize": 20,
    "totalCount": 30,
    "retCode": 0,
    "retMsg": "success"
}
```

``` json
https://iot.universal-space.cn//api/unis/stores/storesList?id=4531

{
    "data": {
        "store_id": 4531,
        "store_latitude": 38.915231,
        "store_logo": "https://static.universal-space.cn/images/20210719/1626657087-c6212e0fe130d360c8fd9efb4a975e6219FrFjmwSRV6FZGEXtZ3ZwcQ896cXUcB.png",
        "link": "https://iot.universal-space.cn/html/youyibao/share_shop.html?storeId=4531&t=1628079806",
        "store_address": "沙河口区西安路103-9号中央大道旅游文化购物中心",
        "brand_name": "",
        "brand_id": 0,
        "head_image": "https://static.universal-space.cn/images/20210719/1626657090-c6212e0fe130d360c8fd9efb4a975e62U9bESei9hMLVpp4FOhqlYAVwdJv9O4hg.png",
        "store_mobile": "",
        "STATUS": 0,
        "cityName": "大连市",
        "store_longitude": 121.587279,
        "store_name": "东方英雄（中央大道店）",
        "provinceName": "辽宁省",
        "gallery": "",
        "countyName": "沙河口区"
    },
    "retCode": 0,
    "retMsg": "success"
}
```

``` json
https://iot.universal-space.cn//api/unis/stores/activityListData?storeid=4531&type=1&pageNo=1&pageSize=1

{
    "data": [],
    "length": 0,
    "pageNo": 1,
    "pageSize": 1,
    "totalCount": 0,
    "retCode": 0,
    "retMsg": "success"
}
```

``` json
https://iot.universal-space.cn//api/unis/stores/comboListData?storeid=4531&pageNo=1&pageSize=20

{
    "data": [],
    "pageNo": 1,
    "length": 0,
    "pageSize": 20,
    "totalCount": 0,
    "retCode": 0,
    "retMsg": "success"
}
```

### 更换头像

``` json
https://iot.universal-space.cn//api/marv/wacca/getUserIconList?pageNo=1&pageSize=50

{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "pageNo": 1,
    "pageSize": 20,
    "totalPage": 1,
    "totalSize": 20,
    "data": [
        {
            "iconId": 102084,
            "iconName": "称霸升级关卡『VII』 ",
            "description": "升级关卡<br>阶段 VII 通关",
            "iconRarity": 2,
            "iconUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/icon/102084.png"
        },
        {
            "iconId": 102048,
            "iconName": "欢迎来到天国",
            "description": "1次游玩时歌曲的难度HARD以上而且达成Full Combo",
            "iconRarity": 4,
            "iconUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/icon/102048.png"
        },
        {
            "iconId": 102047,
            "iconName": "伊莉莎白",
            "description": "1次游玩时歌曲的难度HARD以上而且达成SSS",
            "iconRarity": 4,
            "iconUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/icon/102047.png"
        },
        {
            "iconId": 102027,
            "iconName": "伊莉莎白",
            "description": "玩200次歌曲",
            "iconRarity": 2,
            "iconUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/icon/102027.png"
        },
        {
            "iconId": 102074,
            "iconName": "和服伊莉莎白",
            "description": "期间中游戏之后获得\r2021/02/01 07:00:00 ～ 2021/02/20 06:59:59",
            "iconRarity": 2,
            "iconUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/icon/102074.png"
        },
        {
            "iconId": 102050,
            "iconName": "TANO*C",
            "description": "HARDCORE TANO*C级别的歌曲进行50次挑战",
            "iconRarity": 2,
            "iconUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/icon/102050.png"
        },
        {
            "iconId": 102083,
            "iconName": "称霸升级关卡『VI』 ",
            "description": "升级关卡<br>阶段 VI 通关",
            "iconRarity": 2,
            "iconUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/icon/102083.png"
        },
        {
            "iconId": 102082,
            "iconName": "称霸升级关卡『V』 ",
            "description": "升级关卡<br>阶段 V 通关",
            "iconRarity": 2,
            "iconUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/icon/102082.png"
        },
        {
            "iconId": 102078,
            "iconName": "称霸升级关卡『I』 ",
            "description": "升级关卡<br>阶段 I 通关",
            "iconRarity": 1,
            "iconUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/icon/102078.png"
        },
        {
            "iconId": 102026,
            "iconName": "那家伙",
            "description": "玩100次歌曲",
            "iconRarity": 2,
            "iconUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/icon/102026.png"
        },
        {
            "iconId": 102024,
            "iconName": "解锁人",
            "description": "解锁20首歌曲",
            "iconRarity": 2,
            "iconUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/icon/102024.png"
        },
        {
            "iconId": 102054,
            "iconName": "垂头丧气狗",
            "description": "达成A级别以下2次",
            "iconRarity": 3,
            "iconUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/icon/102054.png"
        },
        {
            "iconId": 102025,
            "iconName": "羽毛",
            "description": "玩50次歌曲",
            "iconRarity": 2,
            "iconUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/icon/102025.png"
        },
        {
            "iconId": 102055,
            "iconName": "『輪』",
            "description": "进行联机玩一次",
            "iconRarity": 2,
            "iconUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/icon/102055.png"
        },
        {
            "iconId": 102029,
            "iconName": "齿轮",
            "description": "获得难度HARD以上而且8次Full Combo",
            "iconRarity": 3,
            "iconUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/icon/102029.png"
        },
        {
            "iconId": 102076,
            "iconName": "徽章",
            "description": "通过基本纹章  4次之后获得",
            "iconRarity": 2,
            "iconUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/icon/102076.png"
        },
        {
            "iconId": 102028,
            "iconName": "般若",
            "description": "获得难度HARD以上而且SS以上的5首歌曲",
            "iconRarity": 3,
            "iconUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/icon/102028.png"
        },
        {
            "iconId": 102023,
            "iconName": "明星",
            "description": "玩5次歌曲",
            "iconRarity": 1,
            "iconUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/icon/102023.png"
        },
        {
            "iconId": 102002,
            "iconName": "WACCA键盘",
            "description": "初期持有",
            "iconRarity": 1,
            "iconUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/icon/102002.png"
        },
        {
            "iconId": 102001,
            "iconName": "WACCA LOGO",
            "description": "初期持有",
            "iconRarity": 1,
            "iconUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/icon/102001.png"
        }
    ]
}
```

### 成就称号

``` json
https://iot.universal-space.cn//api/marv/wacca/getUserTitleList?pageNo=1&pageSize=50&titleType=1

{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "pageNo": 1,
    "pageSize": 32,
    "totalPage": 1,
    "totalSize": 32,
    "data": [
        {
            "titleType": 1,
            "titleName": "WACCA S关卡 VII过关!",
            "titleRarity": 2,
            "titleId": 10104155,
            "description": "升级关卡关卡VII通关"
        },
        {
            "titleType": 1,
            "titleName": "我们的战斗现在才开始!",
            "titleRarity": 2,
            "titleId": 10104166,
            "description": "通过基本闸门12来获得"
        },
        {
            "titleType": 1,
            "titleName": "您玩得好棒喔",
            "titleRarity": 3,
            "titleId": 10104011,
            "description": "达成ALL Marvelous"
        },
        {
            "titleType": 1,
            "titleName": "速度狂人",
            "titleRarity": 2,
            "titleId": 10104056,
            "description": "玩过50次超快速歌曲。"
        },
        {
            "titleType": 1,
            "titleName": "我好像有点强",
            "titleRarity": 1,
            "titleId": 10104052,
            "description": "玩家等级到达30。"
        },
        {
            "titleType": 1,
            "titleName": "我真的通关了「S」级以上",
            "titleRarity": 2,
            "titleId": 10104061,
            "description": "从HARD难易度达成100次S级的纪录"
        },
        {
            "titleType": 1,
            "titleName": "Vocaloid是我的偶像",
            "titleRarity": 2,
            "titleId": 10104019,
            "description": "游玩vocaloid的歌曲时，达成50次 S级的成绩。"
        },
        {
            "titleType": 1,
            "titleName": "我通过了SS级",
            "titleRarity": 3,
            "titleId": 10104006,
            "description": "从EXPERT难易度达成30次SS级的纪录"
        },
        {
            "titleType": 1,
            "titleName": "POP玩家",
            "titleRarity": 2,
            "titleId": 10104038,
            "description": "游玩动画/ 流行歌的歌曲时，达成50次 S级的成绩。"
        },
        {
            "titleType": 1,
            "titleName": "坚持直到我觉得厌烦了",
            "titleRarity": 2,
            "titleId": 10104057,
            "description": "连续10次游玩同一首歌曲。"
        },
        {
            "titleType": 1,
            "titleName": "我是爱动漫歌曲的御宅族",
            "titleRarity": 2,
            "titleId": 10104016,
            "description": "游玩动画/ 流行歌歌曲30次"
        },
        {
            "titleType": 1,
            "titleName": "初赛大成功",
            "titleRarity": 1,
            "titleId": 10104165,
            "description": "通过基本闸门10来获得"
        },
        {
            "titleType": 1,
            "titleName": "WACCA S关卡 VI过关!",
            "titleRarity": 2,
            "titleId": 10104154,
            "description": "升级关卡关卡VI通关"
        },
        {
            "titleType": 1,
            "titleName": "WACCA S关卡 V过关!",
            "titleRarity": 2,
            "titleId": 10104153,
            "description": "升级关卡关卡V通关"
        },
        {
            "titleType": 1,
            "titleName": "WACCA S关卡 I过关!",
            "titleRarity": 1,
            "titleId": 10104149,
            "description": "升级关卡关卡I通关"
        },
        {
            "titleType": 1,
            "titleName": "快点决定吧",
            "titleRarity": 1,
            "titleId": 10104058,
            "description": "试过5次重选歌曲才开始游玩。"
        },
        {
            "titleType": 1,
            "titleName": "我超爱Vocaloid",
            "titleRarity": 2,
            "titleId": 10104015,
            "description": "游玩vocaloid的歌曲30次。"
        },
        {
            "titleType": 1,
            "titleName": "HARDCORE好开森",
            "titleRarity": 2,
            "titleId": 10104018,
            "description": "游玩HARDCORE TANO*C的歌曲30次。"
        },
        {
            "titleType": 1,
            "titleName": "我的战斗现在才开始",
            "titleRarity": 2,
            "titleId": 10104054,
            "description": "玩过90次HARD以上的难易度。"
        },
        {
            "titleType": 1,
            "titleName": "我的等级终于到10啦",
            "titleRarity": 1,
            "titleId": 10104014,
            "description": "玩家等级到达10。"
        },
        {
            "titleType": 1,
            "titleName": "今天也来玩",
            "titleRarity": 1,
            "titleId": 10104164,
            "description": "通过基本闸门8来获得"
        },
        {
            "titleType": 1,
            "titleName": "为了与强者相遇而来",
            "titleRarity": 1,
            "titleId": 10104049,
            "description": "玩过1次多人模式(对战)。"
        },
        {
            "titleType": 1,
            "titleName": "配饰爱好者",
            "titleRarity": 2,
            "titleId": 10104055,
            "description": "达成使用头像来游玩5次。"
        },
        {
            "titleType": 1,
            "titleName": "习惯了这幅身体",
            "titleRarity": 1,
            "titleId": 10104051,
            "description": "琉过15次NORMAL以上的难易度。"
        },
        {
            "titleType": 1,
            "titleName": "第一次FullCombo!",
            "titleRarity": 2,
            "titleId": 10104012,
            "description": "达成Full Combo"
        },
        {
            "titleType": 1,
            "titleName": "闸门打开",
            "titleRarity": 1,
            "titleId": 10104163,
            "description": "通过基本闸门2来获得"
        },
        {
            "titleType": 1,
            "titleName": "只差一点点",
            "titleRarity": 1,
            "titleId": 10104013,
            "description": "达成Missless"
        },
        {
            "titleType": 1,
            "titleName": "开始WACCA S囉!",
            "titleRarity": 1,
            "titleId": 10104162,
            "description": "通过基本闸门1来获得"
        },
        {
            "titleType": 1,
            "titleName": "快邀我玩多人模式",
            "titleRarity": 1,
            "titleId": 10104005,
            "description": "最初持有"
        },
        {
            "titleType": 1,
            "titleName": "Welcome to WACCA!",
            "titleRarity": 1,
            "titleId": 10104003,
            "description": "最初持有"
        },
        {
            "titleType": 1,
            "titleName": "第一次玩WACCA",
            "titleRarity": 1,
            "titleId": 10104002,
            "description": "最初持有"
        },
        {
            "titleType": 1,
            "titleName": "来宾",
            "titleRarity": 1,
            "titleId": 10104001,
            "description": "最初持有"
        }
    ]
}
```

### 特殊称号

``` json
https://iot.universal-space.cn//api/marv/wacca/getUserTitleList?pageNo=1&pageSize=20&titleType=2

{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "pageNo": 1,
    "pageSize": 0,
    "totalPage": 1,
    "totalSize": 0
}
```

### VIP 套餐

``` json
https://iot.universal-space.cn//api/marv/wacca/vipPackageList

{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "pageNo": 1,
    "pageSize": 30,
    "totalPage": 1,
    "totalSize": 1,
    "data": [
        {
            "id": "6",
            "remarks": "",
            "createDate": "2020-08-31 08:20:29",
            "updateDate": "2021-01-27 17:24:50",
            "packageName": "VIP会员权限（30次）",
            "vipCount": "30",
            "limit": 0,
            "price": "1500",
            "enable": "1",
            "sortNo": "2"
        }
    ]
}
```

### 华卡音舞商店

``` json
https://iot.universal-space.cn//api/marv/wacca/goodsList?

{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "pageNo": 1,
    "pageSize": 30,
    "totalPage": 1,
    "totalSize": 3,
    "data": [
        {
            "id": "2001",
            "remarks": "",
            "createDate": "2020-02-26 13:43:43",
            "updateDate": "2020-07-10 10:27:29",
            "goodsName": "Boost Badge",
            "goodsImage": "https://yyb-oss.universal-space.cn/imgs/wacca/icon_goods_bg_1.png",
            "itemType": "13",
            "itemId": 109001,
            "itemNum": "1",
            "price": "100",
            "enable": "1",
            "sortNo": "1",
            "description": "通过游玩歌曲，2倍获取WP点数，2倍获取闸门点数。"
        },
        {
            "id": "3001",
            "remarks": "",
            "createDate": "2020-02-26 13:44:15",
            "updateDate": "2020-07-10 10:28:22",
            "goodsName": "Boost Badge S",
            "goodsImage": "https://yyb-oss.universal-space.cn/imgs/wacca/icon_goods_bg_2.png",
            "itemType": "13",
            "itemId": 109002,
            "itemNum": "1",
            "price": "200",
            "enable": "1",
            "sortNo": "2",
            "description": "通过游玩歌曲，3.1倍获取WP点数，3.1倍获取闸门点数。"
        },
        {
            "id": "4001",
            "remarks": "",
            "createDate": "2020-02-26 13:44:57",
            "updateDate": "2020-06-29 13:43:50",
            "goodsName": "EX Ticket",
            "goodsImage": "https://yyb-oss.universal-space.cn/imgs/wacca/icon_goods_bg_3.png",
            "itemType": "9",
            "itemId": 106002,
            "itemNum": "1",
            "price": "100",
            "enable": "1",
            "sortNo": "3",
            "description": "用于EXPERT难度曲目开放，玩家游戏中选择玩EXPERT难度曲目时使用。"
        }
    ]
}
```

### 播放歌曲获得的评价

``` json
https://iot.universal-space.cn//api/marv/wacca/userMusicRate?

{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "data": {
        "masterCount": 1, // Master
        "fullcomboCount": 104, //Full Combo
        "rateSsCount": 187, // SS
        "rateSssCount": 140, // SSS
        "clearCount": 463, // Clear
        "rateSCount": 118, // S
        "misslessCount": 331 // Missless
    }
}
```

### 我的最新战绩

``` json
https://iot.universal-space.cn//api/mns/mnsGame/recordDetail?machineId=8340&scoreId=1644390

{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "data": {
        "scoreDetail": {
            "modeName": "单人模式",
            "comboCount": 147, // 连击数
            "gameDate": "2021-07-31 19:05:51",
            "recordPage": "/pages/wacca/wacca-detail",
            "productName": "华卡音舞",
            "machineName": "华卡音舞",
            "score": 914667, // 游戏得分
            "productImage": "https://static.universal-space.cn/images/20210225/1614238244-057dcd8807a598746053dfd049b76eeeW9kj2iIfL3P6in4TmlMMzqhnH1mQwN5p.jpg",
            "musicId": 1242,
            "goodCount": 16,
            "storeName": "东方英雄（中央大道店）",
            "musicGrade": 3,
            "scoreId": 1644390,
            "statisPage": "/pages/wacca/wacca-statis",
            "productId": 3160,
            "musicRate": "S", // 评价
            "storeId": 4531,
            "greatCount": 120,
            "musicName": "GOODWORLD", // 曲目
            "marvelousCount": 594,
            "machineId": 8340,
            "musicGradeName": "Expert", // 难度
            "artistName": "EBIMAYO",
            "musicImage": "https://yyb-oss.universal-space.cn/imgs/wacca/jacket/uT_J_S01_242.png",
            "missCount": 20
        },
        "getItems": {
            "titleList": [],
            "iconList": [],
            "trophyList": []
        }
    }
}
```

### 错误 machineId

``` json
https://iot.universal-space.cn//api/mns/mnsGame/recordDetail?machineId=8341&scoreId=1644390

{
    "code": 30002,
    "message": "找不到对应的游戏记录",
    "detail": "找不到对应的游戏记录",
    "retCode": 30002,
    "retMsg": "找不到对应的游戏记录"
}
```

### 无 machineId

``` json
https://iot.universal-space.cn//api/mns/mnsGame/recordDetail?scoreId=1644390

{
    "code": 2001,
    "message": "字段校验错误",
    "retCode": 2001,
    "retMsg": "字段校验错误"
}
```

### 我的综合排名

``` json
https://iot.universal-space.cn//api/marv/wacca/myStatisRank?musicGrade=2&musicId=1242

{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "data": {
        "trophyCount": 0, // 奖杯数
        "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/F5cBVYtv8xn9OibEFKPkrdqaLSjdic6zwKLG2RLBVXB4to8lWtg5TuIH4X3jvqLnyFRg2NKiausFM1Eu07mhGdRVg/132",
        "nickName": "远哥制造",
        "titleCount": 0, // 称号数
        "rank": 131, // 排名
        "totalScore": 989373, // 综合得分
        "musicCount": 1
    }
}
```

### 全国排名-NORMAL

``` json
https://iot.universal-space.cn//api/marv/wacca/statisRank?pageNo=1&pageSize=10&musicGrade=1

{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "data": {
        "rankInfo": {
            "trophyCount": 27,
            "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/F5cBVYtv8xn9OibEFKPkrdqaLSjdic6zwKLG2RLBVXB4to8lWtg5TuIH4X3jvqLnyFRg2NKiausFM1Eu07mhGdRVg/132",
            "nickName": "远哥制造",
            "titleCount": 32,
            "rank": 192,
            "totalScore": 11835892,
            "musicCount": 12
        },
        "rankList": [
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/8lgkgtM4OKbOD0GT11xickEb4nt0yICa8FxUm3JUjjQ3KNdfcFhb5m3n6Pq9wMmQ8g7ibfz6xu6ia2zovibRia0TG1g/132",
                "nickName": "爱子",
                "titleCount": 77,
                "rank": 1,
                "totalScore": 142000000,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83eolH95K8wrIQFjMqw240IyiboBBicQJTnopdibpdp9Fib9jsSial70haWJ7B6Ts0AC6lBWjYXZYq6YobkQ/132",
                "nickName": "Elizabeth",
                "titleCount": 69,
                "rank": 2,
                "totalScore": 142000000,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/w6PB0WPSSfLtdcQ62mrjF3Xy9y75ZN7GhlOrHb6wZiapaKiciceFFNecRf9QpaVzRSVz7OFpicAFMx4y3O9Yic4k3zA/132",
                "nickName": "谜之势力",
                "titleCount": 60,
                "rank": 3,
                "totalScore": 142000000,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJhBxw8QqhH2xT9kJMO5C6a69EF9zUcfsPEzgezJ03uZHgTvGYCWDO9iah5H6C7CO10LomW09niaohg/132",
                "nickName": "Fluorine0",
                "titleCount": 69,
                "rank": 4,
                "totalScore": 127003827,
                "musicCount": 128
            },
            {
                "trophyCount": 25,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/3tYWPY6IEzdY1b6Zo1v1oER0fPykicjHjFjJZe8u6N0ZTG8ZzzNjeVvyJXAsIYnkuWdutcVPD7q8yU34ibz3ynSQ/132",
                "nickName": "Kamijou Yary",
                "titleCount": 26,
                "rank": 5,
                "totalScore": 125735883,
                "musicCount": 134
            },
            {
                "trophyCount": 30,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83er2MjZ3eSUVCA1icSc46aj6icERO6qXCNCmibfOIdic1WEd0qibAMPmymx8SL0XbfRcSLIEPibHSuEeMNhw/132",
                "nickName": "婷婷不会打音游",
                "titleCount": 43,
                "rank": 6,
                "totalScore": 100364187,
                "musicCount": 101
            },
            {
                "trophyCount": 30,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTIzvTIj6cOlXV7S7eSnMAyGAmqFiaRxzM7ZjKI7PRxf0FfYo9agyVV19icM5TOluaU88gvfLkaeZsWA/132",
                "nickName": "高喜华",
                "titleCount": 37,
                "rank": 7,
                "totalScore": 97971174,
                "musicCount": 103
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJduWD4InqIk8ZzkanGKaPicnRfz15jD93bwh3PLbNfic9Fg8dzdGYQmkClqLFU8vaLibduwp2XdWib7w/132",
                "nickName": "炎凰",
                "titleCount": 63,
                "rank": 8,
                "totalScore": 97920752,
                "musicCount": 100
            },
            {
                "trophyCount": 15,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/7DL88WEw0QuGxfE22zba8xss2JYQGg96LSVr57ibyZ4zUjicJAiahZVPuFnyU1ibfrqKTyGCN5NiaceEJEs9W26RSow/132",
                "nickName": "湖南李曜",
                "titleCount": 13,
                "rank": 9,
                "totalScore": 91868489,
                "musicCount": 102
            },
            {
                "trophyCount": 16,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/RSuROwPtDb7jptXibRk27qfAICPFkanlou6n8m2SdRZEVZhBwkJ2ibFibiaPxUGicNkHZy16uVDsZ1A3XB3Rgsb9ibIw/132",
                "nickName": "初音",
                "titleCount": 16,
                "rank": 10,
                "totalScore": 89664561,
                "musicCount": 110
            }
        ]
    }
}
```

### 全国排名-HARD

``` json
https://iot.universal-space.cn//api/marv/wacca/statisRank?pageNo=1&pageSize=100&musicGrade=2

{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "data": {
        "rankInfo": {
            "trophyCount": 27,
            "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/F5cBVYtv8xn9OibEFKPkrdqaLSjdic6zwKLG2RLBVXB4to8lWtg5TuIH4X3jvqLnyFRg2NKiausFM1Eu07mhGdRVg/132",
            "nickName": "远哥制造",
            "titleCount": 32,
            "rank": 66,
            "totalScore": 131020840,
            "musicCount": 134
        },
        "rankList": [
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/8lgkgtM4OKbOD0GT11xickEb4nt0yICa8FxUm3JUjjQ3KNdfcFhb5m3n6Pq9wMmQ8g7ibfz6xu6ia2zovibRia0TG1g/132",
                "nickName": "爱子",
                "titleCount": 77,
                "rank": 1,
                "totalScore": 142000000,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83eolH95K8wrIQFjMqw240IyiboBBicQJTnopdibpdp9Fib9jsSial70haWJ7B6Ts0AC6lBWjYXZYq6YobkQ/132",
                "nickName": "Elizabeth",
                "titleCount": 69,
                "rank": 2,
                "totalScore": 141978092,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/w6PB0WPSSfLtdcQ62mrjF3Xy9y75ZN7GhlOrHb6wZiapaKiciceFFNecRf9QpaVzRSVz7OFpicAFMx4y3O9Yic4k3zA/132",
                "nickName": "谜之势力",
                "titleCount": 60,
                "rank": 3,
                "totalScore": 141859306,
                "musicCount": 142
            },
            {
                "trophyCount": 30,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJ2Mbk53SAgib2zpibAiaYCLcHSjXdxyD5sGwxep89DibR5bTJYyxWNO2Pl9OwTJ7ZceoiaHiavrbxOHXkA/132",
                "nickName": "Notlan",
                "titleCount": 44,
                "rank": 4,
                "totalScore": 141566742,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/naibWUIibQLNs7JK4oY6p69Sljf03pPEogahC81caLGoL7Ur1r3xVdZ0E6mmwC7B8RSICAlUX97todHnLWNzMQSw/132",
                "nickName": "Lily",
                "titleCount": 80,
                "rank": 5,
                "totalScore": 141505375,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTIzI75KYsI2YRe7ge08vnicFg23N36GdPfJ5yVPhVqsv7D57vEeqN4xLb2FibjDepN7WHLlnYWe4rEQ/132",
                "nickName": "esterTion",
                "titleCount": 57,
                "rank": 6,
                "totalScore": 141469018,
                "musicCount": 142
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJsdnliaPgbibA4ukibicGXztpUQ2pDO6IibXLqx7MxBnPpo4acKKzU0Mf3LmD5ekPH24cgO80WbArLNiaA/132",
                "nickName": "私の天靈",
                "titleCount": 55,
                "rank": 7,
                "totalScore": 141121620,
                "musicCount": 142
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/OD8sSIW7T9GbSloafw11ia5CibNvtB0y47ezY8caPkz50MRQysLkL31n32dDX4tUwhTMqtfUISicL1GMkEBoLfpUw/132",
                "nickName": "atsku",
                "titleCount": 60,
                "rank": 8,
                "totalScore": 140993162,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/gy1fxGWA9rt1HqeTia9PjXT4RnVZ6QqECLEA4kiaMAWaRbbXZlh0LhVzAPaoR3DhJyYsibxxWX3Xkw8dQf0f5Tx2A/132",
                "nickName": "羽灰",
                "titleCount": 76,
                "rank": 9,
                "totalScore": 140904816,
                "musicCount": 142
            },
            {
                "trophyCount": 29,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/cNh1E8c4LgXgGicjaQdt1YYNl1GhZ1Tp2CtYK9ZPy8RPX4vforEVFINSkBmwyQdONa8yib7XrRibhRKABpP9DDmoA/132",
                "nickName": "kobowade",
                "titleCount": 36,
                "rank": 10,
                "totalScore": 140828820,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/O7FdsFsjE6Oic69O5UnjSqck150UjnlzpPZxXjuJX52VU8GfJ9OSiboMJBVPSCWNrib5nicx5eMobz8ibs4icdIcDSpw/132",
                "nickName": "uytc",
                "titleCount": 52,
                "rank": 11,
                "totalScore": 140720796,
                "musicCount": 142
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/NzM9iawsXBWCZF7drgq8vLNJ1SyG0zrX8amWMyLlPXwWNmdwXlNTrBt3PIPHCHdichtx5KvR1jOMVf1GLmqoV4XQ/132",
                "nickName": "蛋挞poi",
                "titleCount": 51,
                "rank": 12,
                "totalScore": 140577414,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/FvTzE5EFdutKUIGUdmORYrOUNun6T6ZdxVowRMicEHJPc7w49EibKqpsFhZotxtvicOYNyyusibibSkvRmKotkXDjibg/132",
                "nickName": "MarnoLos",
                "titleCount": 77,
                "rank": 13,
                "totalScore": 140511878,
                "musicCount": 142
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKEuJztGnlsCvLGUgLy8TXuGgkpiaoXKIV0ZAQyia1e7Rw7ruEdKb034vibrSlI3tfA7JTreqwZIVwIg/132",
                "nickName": "Paul",
                "titleCount": 51,
                "rank": 14,
                "totalScore": 140306264,
                "musicCount": 142
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTI0vVD9myNBBVsuUravMwFJq1tqDwkjlG7by13jLmScujKjbLFGVEONmjZlKRAnUsmV6bcsXQQphA/132",
                "nickName": "清良",
                "titleCount": 57,
                "rank": 15,
                "totalScore": 140088950,
                "musicCount": 142
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/pIvEJIUsvHJfCnFu6icKHTiaPZeb1zlyGNpSR5ibwB0B9tZW3zeA7phwJu8ufwQPKc3tlJg638ODic8wkicpvyb8KAw/132",
                "nickName": "萌菜",
                "titleCount": 58,
                "rank": 16,
                "totalScore": 139983116,
                "musicCount": 142
            },
            {
                "trophyCount": 27,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83epg8gzkbqDlONwbC7PM6jdm5DTiaZeWRv2KbGiaznPjSr9edhnibmMokWjhq5KiajDuTxibnSLxOIFQic0g/132",
                "nickName": "秋海天翼",
                "titleCount": 27,
                "rank": 17,
                "totalScore": 139879898,
                "musicCount": 142
            },
            {
                "trophyCount": 30,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/TUkpMZNW6HYY48pRxFoFWf4icf6uInR3xucujUr3CjgWiaZAq6WxfxIesKvd4hLCS0XIuCBXzdJAN0uhhYpsiaP4g/132",
                "nickName": "Fishy",
                "titleCount": 36,
                "rank": 18,
                "totalScore": 139859122,
                "musicCount": 142
            },
            {
                "trophyCount": 28,
                "avatarUrl": "",
                "nickName": "毕义鑫",
                "titleCount": 32,
                "rank": 19,
                "totalScore": 139737772,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKEwNS5mqPzcTNzbWcgI9U4sAD9AsZFC0pJhDkhAf7WUcaq7DM99KT3LDRg7kaD22xu5Uw0XX8uCQ/132",
                "nickName": "教主",
                "titleCount": 61,
                "rank": 20,
                "totalScore": 139590200,
                "musicCount": 141
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKibqX2nPhYJDWDibGmhKdzxfxwiapK0X6mNVfZmOMuvkLZ5kH6dmPrHTmwubICTtoD9e4lspsRicNdtg/132",
                "nickName": "你懂得",
                "titleCount": 48,
                "rank": 21,
                "totalScore": 139238714,
                "musicCount": 142
            },
            {
                "trophyCount": 27,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKa1cD8I0DPeia7w0thWj7oInAFZffa9e2TXaKKA0vZibxvaH6ibYZB3PYiaJXnFux5JgKDs3G3SnRy9Q/132",
                "nickName": "zyx",
                "titleCount": 33,
                "rank": 22,
                "totalScore": 139152562,
                "musicCount": 142
            },
            {
                "trophyCount": 30,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/olAL7kYlFqJB7B3tZjOvB5f3v7aDmdWnH1fkFsZp8mbkzh2zsj19N9Dfbia7ErOibhia5zHb15I9PUrRM3M7FiansQ/132",
                "nickName": "莉莉踩我",
                "titleCount": 42,
                "rank": 23,
                "totalScore": 139117306,
                "musicCount": 142
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/dcqekwibicaDDCOJ6AH6smQr24daZCBgKaVC3FgRLrHdABedLqsZK5f27yvpa6O9UZ6d9J5PV39HYk8Io1Kkkplw/132",
                "nickName": "小诺",
                "titleCount": 71,
                "rank": 24,
                "totalScore": 138904531,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/ts4U7Bn2aPq6HrUic47oNA94MkgL1h7bUf43bfb7SltEXXNOLgxyXl6SldlQkQ6t3Evibxa8Zxb3JicLUJfurCRdg/132",
                "nickName": "xuan9906",
                "titleCount": 58,
                "rank": 25,
                "totalScore": 138876175,
                "musicCount": 142
            },
            {
                "trophyCount": 27,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTK3HJD1CfyeTtwuRcFeo7Mx3cBhphj9qgzfEvibokOJIX0ZiaLQTPp6Be5geJAsQHIph7magcacZzvA/132",
                "nickName": "RINちゃん",
                "titleCount": 33,
                "rank": 26,
                "totalScore": 138814454,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTLcg2RhOQrtibxcaNJ72N8k03ncZmoHBz33OibicKJ6BcbylRSY5iakFwVxn1YXCERtricEvqMNcyLVvpQ/132",
                "nickName": "🤔",
                "titleCount": 62,
                "rank": 27,
                "totalScore": 138767945,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKOlCicc2o6FWmer1ytbFfjkEnHg04ffibCTqsdT2EQSnxMDpycib11Fghx7p311T8jn3uPicntCTXutQ/132",
                "nickName": "Dirtfuyan",
                "titleCount": 53,
                "rank": 28,
                "totalScore": 138691675,
                "musicCount": 142
            },
            {
                "trophyCount": 27,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJ3Ge8MC1jyyv41WWvn0G9e1P7vd626lnbCtJ41KRHRkibatscWhU9JZ38myUAAibE56BfQ8ibK6KD8w/132",
                "nickName": "XND",
                "titleCount": 31,
                "rank": 29,
                "totalScore": 138576024,
                "musicCount": 142
            },
            {
                "trophyCount": 27,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/IKLN2Wl8eL5iaW5pXjjGXD64FPopuMY1wFOg0pAoaqMWENWuwqJ1SsDepKltwYicTIQ2gUIhEsyhZfiaT9yx2c7Lw/132",
                "nickName": "不灭的灯",
                "titleCount": 33,
                "rank": 30,
                "totalScore": 138541295,
                "musicCount": 140
            },
            {
                "trophyCount": 29,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/ZibrsIVUo9XWFSlzCKVCvD9sJJHK00z3OfVtibykUibTvibJbr0twicA7O7f9oLjYM1g8KQXPOgPazATia5JSrduBP5Q/132",
                "nickName": "Vins子规",
                "titleCount": 51,
                "rank": 31,
                "totalScore": 138483070,
                "musicCount": 142
            },
            {
                "trophyCount": 29,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/iaoNeSEppgLWFrKWVJX8SGIFbrr1MTiaOpAZTlhA35QzotTneiaRGra5Np4e6Ziczk6ufe7VZN1nOY459HuXq6Tp4g/132",
                "nickName": "kumoko",
                "titleCount": 33,
                "rank": 32,
                "totalScore": 138357169,
                "musicCount": 142
            },
            {
                "trophyCount": 30,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83eoPFrT3DYicTRsQxoHxYBS768ATMH3ic5uTcbwIXbOHQw1FknzYBaLz76nzY7KqVZ3bzyiaXk4mEw2sA/132",
                "nickName": "大现充",
                "titleCount": 41,
                "rank": 33,
                "totalScore": 138335954,
                "musicCount": 142
            },
            {
                "trophyCount": 26,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/saVu5SAqXRdQa4flXFQqIesA8k09rREhAcd4RzzOvpqGvNUROCg4UultMQzDXcw98k349IoXZgurlFTFkeJUZw/132",
                "nickName": "sakuya",
                "titleCount": 26,
                "rank": 34,
                "totalScore": 138282094,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/JDXKvx8RWYWcCXBIwlMZBh488Kh3pF26uzzOIYd7RtqkTIZP8ia1DQtCaobppMlnD3UUpLLYJfsiaNGtxRfEJfMQ/132",
                "nickName": "joker wu",
                "titleCount": 71,
                "rank": 35,
                "totalScore": 138242640,
                "musicCount": 142
            },
            {
                "trophyCount": 30,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/JfALOzvXqYrmCx2xnmBYQibTv85CIXWYUqYT1gPXCmDL0lSo47IicOiaLsjwuh3jn7ITibJGtf8icTibicKoydbsHPRlQ/132",
                "nickName": "TKas",
                "titleCount": 38,
                "rank": 36,
                "totalScore": 138210144,
                "musicCount": 142
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTL8GV06roPeF4kXUQhUtdeRQP2eP30pA3XiaJiaicDNvuOAZ4wPolwGFGDvEZtnWnak4lXOdcnlSf5CA/132",
                "nickName": "凉忆忆忆",
                "titleCount": 47,
                "rank": 37,
                "totalScore": 138170424,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTIv6jMib7Isiarm8iaUiagtG7wmk3sCA5FQzLnQErQ30Yt9Y53mibYYjzXdnw5icgzficdoEyaxf0nWAdMow/132",
                "nickName": "誰 ですか",
                "titleCount": 56,
                "rank": 38,
                "totalScore": 138068602,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/kyd037ZVZrs1Jfx7ibpZ4AfPG6aRgWrdzBzbqZAZibVhicNd0g0VNOsjyicyJd9HxGtJLUtQsVkWhYox8cibvNNLKjw/132",
                "nickName": "HDMI",
                "titleCount": 76,
                "rank": 39,
                "totalScore": 138048811,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/e0Tb7ERmWePRh9ggvJM7rF3ezIsUTE9WVWU73sZnpcQqyvoOliafZY79AqD0uxLXWEUz5SosHfks2duGIsOWszw/132",
                "nickName": "开朗的大树",
                "titleCount": 49,
                "rank": 40,
                "totalScore": 138030131,
                "musicCount": 142
            },
            {
                "trophyCount": 29,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/eZJjEQUCLozlXIib91Op4ID8icLaUgiaZ2rpF4MYpeWzuMPqlsZNy7ECOiaQhb5pU8oicpIcB5f0ictRHkNOoMEXSjWA/132",
                "nickName": "大雄",
                "titleCount": 43,
                "rank": 41,
                "totalScore": 137985672,
                "musicCount": 141
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/TuNq9l1g3GdjN5UqcseNNibduYWtOeC8vSPpzxIF3ElFMFIlr51KZ2iaIVYLaS2oQ5zIa133yOvPUtsnqEmrPgJw/132",
                "nickName": "🍃",
                "titleCount": 45,
                "rank": 42,
                "totalScore": 137966968,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKfsnQHE1LrY4BvOsu8rCcOI8NRP8hIEHnGnbQZ1bmZhAYjSNtuZktOSrnCBicd7beY3Qqb0rOXEibQ/132",
                "nickName": "ArcDanceP",
                "titleCount": 55,
                "rank": 43,
                "totalScore": 137418580,
                "musicCount": 139
            },
            {
                "trophyCount": 30,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/cPtAwg7kpObc7GabApsezHzqXbkicayqEgh7pn36ZxWpRiaVFoE8qrNJC5VW5aibyWWibkicYPy8QaIias2dGYEwTJBA/132",
                "nickName": "风家陈小胖",
                "titleCount": 42,
                "rank": 44,
                "totalScore": 137410738,
                "musicCount": 141
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/3SmMwjZLc8P3Nia0EfXUHKStZ8st9qa0ia7AYUu5GVFTOk0auTDqNiaw40eohvtPdrw5TocVROtVpyuf4BOCnFyiaA/132",
                "nickName": "记得",
                "titleCount": 47,
                "rank": 45,
                "totalScore": 137337030,
                "musicCount": 140
            },
            {
                "trophyCount": 29,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKVibpnjmtjfhvV3t0iclb9tODY7G6PvYicpDbhg0GYzPteibUWUVUSMrBkDduUnKW6UgeD6Yl0j8JlmQ/132",
                "nickName": "自来MIZU",
                "titleCount": 37,
                "rank": 46,
                "totalScore": 137176168,
                "musicCount": 139
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/4sGO9zPqwwuKP7gf4d8ibtpN9HFhVuBeqOXNfJ9swbuA2rgbczHiagXPXoWKCycjrriab2eia9dHQ3fKBfhsgrmnbg/132",
                "nickName": "分からない",
                "titleCount": 50,
                "rank": 47,
                "totalScore": 136018442,
                "musicCount": 137
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/biartx93PmJaMLHv2tQfcicMWHDuSow9JDI1icQnpPDI4w2Ik3LRZBs2gDjIt4RrEExO9s46iafW5odSoPQsFSIZnA/132",
                "nickName": "衰兔子",
                "titleCount": 78,
                "rank": 48,
                "totalScore": 136000000,
                "musicCount": 136
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/RbGf9FKbOibiawfGLTy85yBPEFxQztHib3qjjiatnaiaSZB7KMr1RxicEbCEMyqGRibjtkvISmNZkbTmm9savpy1NJicWQ/132",
                "nickName": "じょたろさん",
                "titleCount": 53,
                "rank": 49,
                "totalScore": 135954643,
                "musicCount": 138
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKaDHPt5uk1yu85FW98icSqDAp8iapRiaPKT9fXJKuVIluorjmQRwe1ad23gwoS6Le4iaQ0nYaXg5hgCQ/132",
                "nickName": "hamzo",
                "titleCount": 38,
                "rank": 50,
                "totalScore": 135947559,
                "musicCount": 139
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKMftIGhYTmQQ5Iibr00OMaxNic7xuUCFAtnutr36FwZMia7J8JQbo623P8xKWicxA9h1z36GiaaNibRc7A/132",
                "nickName": "🎉 huihui酱💋",
                "titleCount": 51,
                "rank": 51,
                "totalScore": 135629116,
                "musicCount": 140
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/AqSIjo8uOAFxXibbYmdhsyIic9TV4Y4FZFOwmjvL7qH64Z9CibEGicZPGqhWOwSDu0GudTD145WicpDic8DhHEtqBLIQ/132",
                "nickName": "Cierran",
                "titleCount": 67,
                "rank": 52,
                "totalScore": 135343676,
                "musicCount": 137
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/oqBmeeufQcTRmqbiaX1OPl3F0IAVoORicUGrwrMQhIEJwJ2lMEubAovePCg3ic4WPfpnXJnHNpbQomhn0WRjV4LDg/132",
                "nickName": "秋千兽.",
                "titleCount": 56,
                "rank": 53,
                "totalScore": 135342670,
                "musicCount": 139
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/rFmVgCg1Rn27zChicwicJYpic3oSFMGDlicCHbF8Kwqial795h1M9JHzVdxbKb9h2yrB9QJzibLVex0qHTMU2ymrAFNA/132",
                "nickName": "かえで",
                "titleCount": 63,
                "rank": 54,
                "totalScore": 134819096,
                "musicCount": 137
            },
            {
                "trophyCount": 29,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/FkV4vBABpfLRLob80Epic5v4CreFAGKOUibZ9Zw6DQGOjpWDBh51nd2qaeXgP9zFZNuaEQrtCXUP2leJZ5veCrng/132",
                "nickName": "k-g-r-（刘奕栩）",
                "titleCount": 38,
                "rank": 55,
                "totalScore": 134591759,
                "musicCount": 138
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKt7x668CACFhrqFViaLedsqPIibaukhnSDr8KXibsQ3XQ7GcfXsYf1zWLbzGCgibmoaybYb0GicooOjEQ/132",
                "nickName": "Athlonsy 2Gen",
                "titleCount": 81,
                "rank": 56,
                "totalScore": 134278885,
                "musicCount": 135
            },
            {
                "trophyCount": 30,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/w6PB0WPSSfLtdcQ62mrjF10qWDeGO9icUT3GNHlic0BKnDrVjHTrryZ72MgpC77KAuaSaCpGGTcXl1CgUicNW66kQ/132",
                "nickName": "Tiger",
                "titleCount": 38,
                "rank": 57,
                "totalScore": 134071248,
                "musicCount": 136
            },
            {
                "trophyCount": 26,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKaYyzoIYTKia8rfvl9RVAvRdxzQGQBCeUIkt6lUF5rPuArbrmjicFxapTicQyCMozTHaGiaibBPbmvz6A/132",
                "nickName": "星辰大海",
                "titleCount": 29,
                "rank": 58,
                "totalScore": 134005141,
                "musicCount": 138
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJh5tnxPfpfpGqzf8icgWJ98IcdZhh1SDiaeicf8McYvtkE8ZGU4UR9YlxFyiayRhYhlh4CWV9YvBFILA/132",
                "nickName": "又菜又爱玩",
                "titleCount": 61,
                "rank": 59,
                "totalScore": 133936436,
                "musicCount": 136
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTINoO2goTTpd0y7ibuf4LG00sD756bv8oYBydWMFicvpkYKC23U3Taf6Su9iaM6qkzsLfvZkW4tlhRFw/132",
                "nickName": "鱼鱼鱼",
                "titleCount": 68,
                "rank": 60,
                "totalScore": 133002299,
                "musicCount": 135
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJhBxw8QqhH2xT9kJMO5C6a69EF9zUcfsPEzgezJ03uZHgTvGYCWDO9iah5H6C7CO10LomW09niaohg/132",
                "nickName": "Fluorine0",
                "titleCount": 69,
                "rank": 61,
                "totalScore": 132988371,
                "musicCount": 133
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/ib10rznyxX8TCh6GYkLcB2hjkcQXz0QeXNp2RH0UEypjWwXXh01KibAcqpxggKtd8icKQic2ymUnan5cxsE4oeHibCg/132",
                "nickName": "白杨",
                "titleCount": 75,
                "rank": 62,
                "totalScore": 132706914,
                "musicCount": 136
            },
            {
                "trophyCount": 28,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/cOqficCQqBwj2Oicrr6y4GouvcP8Ue1pHDm7F9dXYfcCVGhIcCDXLRXLzeoTicMtLUtDW0J7WRJJRPsmSV3WtkCsA/132",
                "nickName": "⑨",
                "titleCount": 29,
                "rank": 63,
                "totalScore": 131923305,
                "musicCount": 137
            },
            {
                "trophyCount": 27,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKVf2qoCNGUs51StDqeFgt5YWUycdqrysTbLLUCVPC36jkbfEQibaIn1pwoayzqE8hmZTezscg6DLg/132",
                "nickName": "夏夜展风飞",
                "titleCount": 29,
                "rank": 64,
                "totalScore": 131744877,
                "musicCount": 139
            },
            {
                "trophyCount": 29,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJHIYEickds6dDYCU0sG0icibicLIia5mYftEd9D2XYaWvnztkZduvVEaicjChKGECFadxgZIeLXRYFumVw/132",
                "nickName": "爵士鼓孤独患者",
                "titleCount": 37,
                "rank": 65,
                "totalScore": 131354656,
                "musicCount": 133
            },
            {
                "trophyCount": 27,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/F5cBVYtv8xn9OibEFKPkrdqaLSjdic6zwKLG2RLBVXB4to8lWtg5TuIH4X3jvqLnyFRg2NKiausFM1Eu07mhGdRVg/132",
                "nickName": "远哥制造",
                "titleCount": 32,
                "rank": 66,
                "totalScore": 131020840,
                "musicCount": 134
            },
            {
                "trophyCount": 28,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83ernicHN4ye7wia54LNDMSiamicP5p17wMChJbmornjKAaKwW0kY9hbAxicI5oN5vT95NPlckiczOMlnsALQ/132",
                "nickName": "POTATO",
                "titleCount": 35,
                "rank": 67,
                "totalScore": 130419185,
                "musicCount": 135
            },
            {
                "trophyCount": 29,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/wmzZdnfEPk962J1rCcK7ve3sS2oUiayiczicuh9k1ralmiaF7bsNf0qr2JPydhcre8uACGeaN7reZV1Et4RCM7Ria1A/132",
                "nickName": "Teaspoooooon",
                "titleCount": 35,
                "rank": 68,
                "totalScore": 130342263,
                "musicCount": 131
            },
            {
                "trophyCount": 28,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/2MtktLrGYEhbZ6b9lhuOH3hraWPDicPtbAYkdF8xatl4qQj2Qrd20kiaaXOzJJoRj5AHVuXgdZkjNktUl2VkkVPQ/132",
                "nickName": "GUEST",
                "titleCount": 39,
                "rank": 69,
                "totalScore": 130119763,
                "musicCount": 135
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83ep10L39bab5TY8ZQBr8BszUS2aMuu0QSMibn41MTFdIDTbcB1DVsTB1nFibFcLSaosDj9pAaY4FSvgQ/132",
                "nickName": "Moriko",
                "titleCount": 62,
                "rank": 70,
                "totalScore": 129985335,
                "musicCount": 132
            },
            {
                "trophyCount": 26,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/V9UEWkXMWYRY7yqmavWzyhGpzJSZ0uL7923QDqQlushPENsD3eyYnv2LC4lsDuUtic2meia05MGZ5kG1OOGQy0Wg/132",
                "nickName": "ELT",
                "titleCount": 24,
                "rank": 71,
                "totalScore": 129937537,
                "musicCount": 132
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/fLhxlXjQicaa8AIeOYtiaNW3kNSn8NTzGmYSia5rTKGyAHmgnDxvy5L2RbMsVCaicyHWIic6lPOd9jxklIgxRGJnIGQ/132",
                "nickName": "M0N4",
                "titleCount": 66,
                "rank": 72,
                "totalScore": 129824577,
                "musicCount": 133
            },
            {
                "trophyCount": 30,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/x3DZMT1g5xxGdkbnxolCHPJf3nTUXWO36p0Twl5K224Iue8Rn8hSHbzHEwibl45ad0VntuqBiakKzQy0Hibu4hPFg/132",
                "nickName": "88503",
                "titleCount": 39,
                "rank": 73,
                "totalScore": 129527381,
                "musicCount": 132
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJROwzRqp5JG4ged8cJ4zy990yh52ickjBTMm33osj5e4AaKib4sGr4mY4BcFKU0ac9aOkMBYWbIzibA/132",
                "nickName": "Mirror",
                "titleCount": 62,
                "rank": 74,
                "totalScore": 129441289,
                "musicCount": 131
            },
            {
                "trophyCount": 26,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83eryUWQeZRLTKAkUt0hEib1VuxuGN5voHYibWxmRYhk3coFIAvmo74AicqqyPMWjv29RWib4yrk28z0tCA/132",
                "nickName": "NaD",
                "titleCount": 32,
                "rank": 75,
                "totalScore": 129008618,
                "musicCount": 132
            },
            {
                "trophyCount": 26,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTLs0BeahyTI9CzBE7u68l13fow3W1ygibODCre8B6DJTEYNhibbbXQkOic0ZbEwVGe8pEg6Y8cicO8S7g/132",
                "nickName": "雨夜",
                "titleCount": 29,
                "rank": 76,
                "totalScore": 128622572,
                "musicCount": 132
            },
            {
                "trophyCount": 26,
                "avatarUrl": "https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTLNhqibQaiaIhz6iaJYnNA6icniaibDn46nCf3fd5v9Bo1uzmafYu8BCCEc1NxdUpDL5aZv73nCFUn8UX9Q/132",
                "nickName": "Seraphim",
                "titleCount": 27,
                "rank": 77,
                "totalScore": 128270845,
                "musicCount": 130
            },
            {
                "trophyCount": 30,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTI6SHHKtX755hEgZxha1B2Cicn6HGLlGnZrASWSV5qv0II6fNWicLDibljpH0l45p1qtv7dfN0libdmKg/132",
                "nickName": "小恐龙开飞机嗷呜嗷呜",
                "titleCount": 43,
                "rank": 78,
                "totalScore": 128244780,
                "musicCount": 131
            },
            {
                "trophyCount": 27,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/hLDKOusTaTaVd6hH7G8cJM1aUZe1fyWsF5HCOSa3SsJ2pbeu7p2DIDUYamN5BjsqUSvtQ0A6vs8Xz8oxxKnhUA/132",
                "nickName": "混合汁",
                "titleCount": 27,
                "rank": 79,
                "totalScore": 127477572,
                "musicCount": 130
            },
            {
                "trophyCount": 26,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/2hwicxHWtLFVjRQpeDTgSbT59RXnpkYt8y52vWKjZzvlCqlu5qG3Ao0gs4NdVuNHEPZmghibcfpPJuWtzCTQPQOg/132",
                "nickName": "RDmas",
                "titleCount": 28,
                "rank": 80,
                "totalScore": 127172847,
                "musicCount": 132
            },
            {
                "trophyCount": 29,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKjqibCZyWVqAFeUv1lAlcuiaN6z7ia3KhKlyfaO8MMpZvMD9eGEEwWqKZxjnj95mAkIZEiayh0Kyy1UA/132",
                "nickName": "千夏",
                "titleCount": 39,
                "rank": 81,
                "totalScore": 127152883,
                "musicCount": 129
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTL2JDCLUlC2zopgJKeeSDwL4ayC04iblkoQguAZszhBShfQrgFNNwDvTv0Iw7yHzOTLg3oQZPiaBfsw/132",
                "nickName": "零儿",
                "titleCount": 47,
                "rank": 82,
                "totalScore": 126969023,
                "musicCount": 131
            },
            {
                "trophyCount": 28,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/bBia1LLVBHndDYmQ0wCkQ7zslvWpX2NJ8H0yicOeTlJibr9CrIU0evAADlAV0nGvOdsic01Cpdk3mWRFLdLlyFudtA/132",
                "nickName": "黄狗",
                "titleCount": 38,
                "rank": 83,
                "totalScore": 126701160,
                "musicCount": 131
            },
            {
                "trophyCount": 27,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/hesyaCgNNme1c83vpbabH7H6iccDkm1sdyRPSYpOAq9xkeFEHsmywbauQFwvvOs5TaviaKIeZLxGqyl5q5AcN9lg/132",
                "nickName": "蝶舞",
                "titleCount": 28,
                "rank": 84,
                "totalScore": 126117662,
                "musicCount": 132
            },
            {
                "trophyCount": 30,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Hch8ichNISO8epB6JohLTsD2NNZRpexDftgE1GeKrcdTqV85FuEZyjKBe4iaQJNG1f22uM9tXSDQIicLnCe5JZSsg/132",
                "nickName": "Unravel",
                "titleCount": 39,
                "rank": 85,
                "totalScore": 125673678,
                "musicCount": 132
            },
            {
                "trophyCount": 30,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83erhIzXT3OTWaA8dKSnF54OjhGWKPEoBeFGibFHSCkopwR05jYIXESR4XscPp7EZy7Y9cX7l6QU9ibjQ/132",
                "nickName": "C.c",
                "titleCount": 42,
                "rank": 86,
                "totalScore": 125436733,
                "musicCount": 127
            },
            {
                "trophyCount": 28,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/dGuicdagYGBHHECEfibCkrkMYU04O5zQwSCb8UAXsV1qQWSezVdnbx0WRyUFt8Guu2eZCTMqvEZMEpypiaxDLtnrg/132",
                "nickName": "梳子",
                "titleCount": 35,
                "rank": 87,
                "totalScore": 125329976,
                "musicCount": 128
            },
            {
                "trophyCount": 25,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/3tYWPY6IEzdY1b6Zo1v1oER0fPykicjHjFjJZe8u6N0ZTG8ZzzNjeVvyJXAsIYnkuWdutcVPD7q8yU34ibz3ynSQ/132",
                "nickName": "Kamijou Yary",
                "titleCount": 26,
                "rank": 88,
                "totalScore": 125264746,
                "musicCount": 133
            },
            {
                "trophyCount": 26,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTItNTM6icrFHjPkL0u62kQicrzfqXpJ9Db68x32kp1nOoT4bjHAdZJx578wwhDtgQ0RjYrClFyBRiaibg/132",
                "nickName": "ろうかん",
                "titleCount": 27,
                "rank": 89,
                "totalScore": 124867934,
                "musicCount": 127
            },
            {
                "trophyCount": 29,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKVkoe7Viae4lsJGGo5jrPpIx62rh5eduaNqBGHer2w3BPD4JSehNO1PFGWpsFKbQKr58tARTJvQUg/132",
                "nickName": "SuPa",
                "titleCount": 37,
                "rank": 90,
                "totalScore": 124593973,
                "musicCount": 128
            },
            {
                "trophyCount": 30,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83er2MjZ3eSUVCA1icSc46aj6icERO6qXCNCmibfOIdic1WEd0qibAMPmymx8SL0XbfRcSLIEPibHSuEeMNhw/132",
                "nickName": "婷婷不会打音游",
                "titleCount": 43,
                "rank": 91,
                "totalScore": 124279460,
                "musicCount": 126
            },
            {
                "trophyCount": 25,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJzdBWzImYq5KWiaic5hc34511FscKFVPaGw7ia4OzGm1hK6VPOM0H418j36fXjNVQOBatkeUIJoAjJw/132",
                "nickName": "Selentia",
                "titleCount": 28,
                "rank": 92,
                "totalScore": 124014963,
                "musicCount": 127
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/PiajxSqBRaEL3l9K6kJe6LVj1BwAdsIakn0MGbyRVKs3oZe0k40Gs7dI6ev8kXCN77uRbkDBTnNZ0B1RsUPnRHQ/132",
                "nickName": "GeNociDeR",
                "titleCount": 63,
                "rank": 93,
                "totalScore": 123913423,
                "musicCount": 125
            },
            {
                "trophyCount": 28,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKHeia1bvDcATLNGiagvJ0TDic3icat8XiazV297deibxDvIGx7SfVIzCa1PcXV0qFfUCmhHpMA2WHPfkEw/132",
                "nickName": "天天",
                "titleCount": 36,
                "rank": 94,
                "totalScore": 123881991,
                "musicCount": 135
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83eribHbF4k0IxZp8f07gYqsBxZn3RyfX6gxMD3CqPKAAmSSicIDLUDPWibnGTSyZYGglSQSnsy8Ehib9rA/132",
                "nickName": "ATA_DRS",
                "titleCount": 74,
                "rank": 95,
                "totalScore": 122895134,
                "musicCount": 124
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/2sjUOeNDGYyfQd13iaFDt865mae4gFIDpkPiasOFic8MzFQpzgRqsY87eIqqwTcFwtTJKer73Nic3nMP8MFz4fTiatQ/132",
                "nickName": "我想当嘉然小姐的狗",
                "titleCount": 52,
                "rank": 96,
                "totalScore": 122608629,
                "musicCount": 125
            },
            {
                "trophyCount": 25,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/WQ9FKrAgj0BlDlV4PZ73ONVMe7kC8xqC59j2h2mtSlx0nFzZjEByTdVibrSlrh9XCE7qAnTTgzMicNpSRkRbdkpg/132",
                "nickName": "Lancer",
                "titleCount": 25,
                "rank": 97,
                "totalScore": 122126859,
                "musicCount": 126
            },
            {
                "trophyCount": 27,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/u954UKCTyyHshPVOu5FAdia0e45rW82XCvE6S5pFoTTYWrd572ZnMfekbRIvJ71J5aMr5hVicHEFy7PvVWRd9ZiaA/132",
                "nickName": "Fuclear_fuel",
                "titleCount": 34,
                "rank": 98,
                "totalScore": 121735998,
                "musicCount": 127
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83erc6IibsNYw3oZPBYXlNRUibC4rwlvBh4Cc5dNZNmOiaQCDW4Js2ZCrzbIabxYVI8dXxgzub8qy3hwNA/132",
                "nickName": "Reisen",
                "titleCount": 59,
                "rank": 99,
                "totalScore": 121298417,
                "musicCount": 122
            },
            {
                "trophyCount": 25,
                "avatarUrl": "https://wx.qlogo.cn/mmopen/vi_32/DYAIOgq83eqDP52r4OGXA7UZP7ccxRNsCnBicpux6tcXzXia6icN7OBCCAgQPkqyXkvWCNFj5VIaRLicqgOZrf2yuw/132",
                "nickName": "登士柏西诺德-陈禹良",
                "titleCount": 22,
                "rank": 100,
                "totalScore": 121018479,
                "musicCount": 123
            }
        ]
    }
}
```

### 全国排名-EXPERT

``` json
https://iot.universal-space.cn//api/marv/wacca/statisRank?pageNo=1&pageSize=10&musicGrade=3

{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "data": {
        "rankInfo": {
            "trophyCount": 27,
            "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/F5cBVYtv8xn9OibEFKPkrdqaLSjdic6zwKLG2RLBVXB4to8lWtg5TuIH4X3jvqLnyFRg2NKiausFM1Eu07mhGdRVg/132",
            "nickName": "远哥制造",
            "titleCount": 32,
            "rank": 1064,
            "totalScore": 35953186,
            "musicCount": 123
        },
        "rankList": [
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83erkNog3JQibEr8VdfJuwABicXyIJMiaQDU3RZyswgUqZI1zQ3BUyM751EwxQHW0HAYnsNxLV13NIUxEg/132",
                "nickName": "Athlon·L",
                "titleCount": 80,
                "rank": 1,
                "totalScore": 141983462,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/biartx93PmJaMLHv2tQfcicMWHDuSow9JDI1icQnpPDI4w2Ik3LRZBs2gDjIt4RrEExO9s46iafW5odSoPQsFSIZnA/132",
                "nickName": "衰兔子",
                "titleCount": 78,
                "rank": 2,
                "totalScore": 141981761,
                "musicCount": 142
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/PiajxSqBRaEIe7HnXYmOgJR5fwVTuV2WxOXFAdykQB7eDRemNbZxj81bkVnZZVGVxFXpNOQKApKNUpKzbDicDxcw/132",
                "nickName": "SepTunE",
                "titleCount": 60,
                "rank": 3,
                "totalScore": 141942857,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJhBxw8QqhH2xT9kJMO5C6a69EF9zUcfsPEzgezJ03uZHgTvGYCWDO9iah5H6C7CO10LomW09niaohg/132",
                "nickName": "Fluorine0",
                "titleCount": 69,
                "rank": 4,
                "totalScore": 141941029,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/FvTzE5EFdutKUIGUdmORYrOUNun6T6ZdxVowRMicEHJPc7w49EibKqpsFhZotxtvicOYNyyusibibSkvRmKotkXDjibg/132",
                "nickName": "MarnoLos",
                "titleCount": 77,
                "rank": 5,
                "totalScore": 141816289,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83epibr0LAy3JF3s09vIp7JZkf7uHib51EicwhbzIOXqWGSE2R9EvnegrnIWFQ6tXGcTrsVQ0kWlygYficw/132",
                "nickName": "Peter the Ho'ney",
                "titleCount": 67,
                "rank": 6,
                "totalScore": 141782255,
                "musicCount": 142
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/mHHFnsv2DPD0pZAvicDI1vsRJGjaxWBSpYZbyboDshnhITiblh77fXJqoWV3ibpvtWSx05KNUvia0EsZJYgCIOFG6g/132",
                "nickName": "试作型衰兔子MkII",
                "titleCount": 72,
                "rank": 7,
                "totalScore": 141725603,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/8lgkgtM4OKbOD0GT11xickEb4nt0yICa8FxUm3JUjjQ3KNdfcFhb5m3n6Pq9wMmQ8g7ibfz6xu6ia2zovibRia0TG1g/132",
                "nickName": "爱子",
                "titleCount": 77,
                "rank": 8,
                "totalScore": 141718574,
                "musicCount": 142
            },
            {
                "trophyCount": 33,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKt7x668CACFhrqFViaLedsqPIibaukhnSDr8KXibsQ3XQ7GcfXsYf1zWLbzGCgibmoaybYb0GicooOjEQ/132",
                "nickName": "Athlonsy 2Gen",
                "titleCount": 81,
                "rank": 9,
                "totalScore": 141704723,
                "musicCount": 142
            },
            {
                "trophyCount": 31,
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83eribHbF4k0IxZp8f07gYqsBxZn3RyfX6gxMD3CqPKAAmSSicIDLUDPWibnGTSyZYGglSQSnsy8Ehib9rA/132",
                "nickName": "ATA_DRS",
                "titleCount": 74,
                "rank": 10,
                "totalScore": 141603362,
                "musicCount": 142
            }
        ]
    }
}
```

``` json
https://iot.universal-space.cn//api/marv/wacca/getMusicInfo?musicId=1031

{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "data": {
        "musicName": "リアル初音ミクの消失", // 歌曲名称
        "artistName": "cosMo＠暴走P", // 艺人名称
        "musicCover": "https://yyb-oss.universal-space.cn/imgs/wacca/jacket/uT_J_S01_031.png",
        "normalLevel": "6",
        "hardLevel": "9",
        "expertLevel": "13"
    }
}
```

### 单曲排行榜

``` json
https://iot.universal-space.cn//api/marv/wacca/musicRank?musicId=1031&pageNo=1&pageSize=10&musicGrade=1

{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "data": {
        "rankInfo": {
            "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/F5cBVYtv8xn9OibEFKPkrdqaLSjdic6zwKLG2RLBVXB4to8lWtg5TuIH4X3jvqLnyFRg2NKiausFM1Eu07mhGdRVg/132",
            "gameDate": "2021-07-08 19:16:25",
            "nickName": "远哥制造",
            "rank": 1,
            "artistName": "cosMo＠暴走P",
            "storeName": "东方英雄（中央大道店）",
            "maxScore": 1000000,
            "musicName": "リアル初音ミクの消失"
        },
        "rankList": [
            {
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/F5cBVYtv8xn9OibEFKPkrdqaLSjdic6zwKLG2RLBVXB4to8lWtg5TuIH4X3jvqLnyFRg2NKiausFM1Eu07mhGdRVg/132",
                "nickName": "远哥制造",
                "rank": 1,
                "storeName": "东方英雄（中央大道店）",
                "maxScore": 1000000,
                "createDate": "2021-07-08 19:16:25"
            },
            {
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/8lgkgtM4OKbOD0GT11xickEb4nt0yICa8FxUm3JUjjQ3KNdfcFhb5m3n6Pq9wMmQ8g7ibfz6xu6ia2zovibRia0TG1g/132",
                "nickName": "爱子",
                "rank": 2,
                "storeName": "大玩家广州海珠万达店",
                "maxScore": 1000000,
                "createDate": "2021-04-04 21:53:31"
            },
            {
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/w6PB0WPSSfLtdcQ62mrjF3Xy9y75ZN7GhlOrHb6wZiapaKiciceFFNecRf9QpaVzRSVz7OFpicAFMx4y3O9Yic4k3zA/132",
                "nickName": "谜之势力",
                "rank": 3,
                "storeName": "奇奇乐园宜昌店",
                "maxScore": 1000000,
                "createDate": "2021-02-07 10:33:05"
            },
            {
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83eolH95K8wrIQFjMqw240IyiboBBicQJTnopdibpdp9Fib9jsSial70haWJ7B6Ts0AC6lBWjYXZYq6YobkQ/132",
                "nickName": "Elizabeth",
                "rank": 4,
                "storeName": "极客森超乐场深圳宝能城店",
                "maxScore": 1000000,
                "createDate": "2021-02-05 21:45:42"
            },
            {
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/DYAIOgq83er2MjZ3eSUVCA1icSc46aj6icERO6qXCNCmibfOIdic1WEd0qibAMPmymx8SL0XbfRcSLIEPibHSuEeMNhw/132",
                "nickName": "婷婷不会打音游",
                "rank": 5,
                "storeName": "PPG潮玩汇",
                "maxScore": 997436,
                "createDate": "2021-03-21 21:24:53"
            },
            {
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKEwNS5mqPzcTNzbWcgI9U4sAD9AsZFC0pJhDkhAf7WUcaq7DM99KT3LDRg7kaD22xu5Uw0XX8uCQ/132",
                "nickName": "教主",
                "rank": 6,
                "storeName": "中山乐趣时代（金鹰店）",
                "maxScore": 994231,
                "createDate": "2021-03-20 18:01:23"
            },
            {
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTIzvTIj6cOlXV7S7eSnMAyGAmqFiaRxzM7ZjKI7PRxf0FfYo9agyVV19icM5TOluaU88gvfLkaeZsWA/132",
                "nickName": "高喜华",
                "rank": 7,
                "storeName": "游艺宝",
                "maxScore": 987500,
                "createDate": "2021-03-05 15:13:44"
            },
            {
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJh5tnxPfpfpGqzf8icgWJ98IcdZhh1SDiaeicf8McYvtkE8ZGU4UR9YlxFyiayRhYhlh4CWV9YvBFILA/132",
                "nickName": "又菜又爱玩",
                "rank": 8,
                "storeName": "风云再起福州店",
                "maxScore": 986859,
                "createDate": "2021-02-21 14:09:53"
            },
            {
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/sNbmVmjmQYfWNwOEP5yfxoHEyIofku5gfticuwS4YmrnGNzJz9IicYYjo7VQrTXatRYlibKicSlFiaKwvB5r0vaSmibw/132",
                "nickName": "凉亭",
                "rank": 9,
                "storeName": "极限主场惠州店",
                "maxScore": 975641,
                "createDate": "2021-04-05 17:46:36"
            },
            {
                "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q1s3tUoYFJezXvEk7Rx9YWLaBBiaibicX0Lxia3dk0Dla5uSvRAqyOvA0ZQPRnJtia7WfV6evfbLrhePib4o5tdiavWQA/132",
                "nickName": "-雪月凝霜-",
                "rank": 10,
                "storeName": "第一回合（杭州城西银泰店）",
                "maxScore": 972756,
                "createDate": "2021-03-07 19:04:00"
            }
        ]
    }
}
```
