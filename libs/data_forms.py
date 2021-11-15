import json

def SKU_form():
    SKU = {
            'DATA': [
                {
                    'SKU_CODE': 'A101110001',
                    'SKU_DESC': 'null',
                    'SKU_DESC_LOCAL': 'null',
                    'ACTIVE': 'true',
                    'STORAGE_TYPE': 'AMBIENT',
                    'STORAGE_CAT_SERVICE': 'GENERAL',
                    'PRODUCT_TYPE': 'NORMAL',
                    'MATERIAL_TYPE': 'STEEL',
                    'PRODUCT_FAMILY_01': 'null',
                    'PRODUCT_FAMILY_02': 'null',
                    'PRODUCT_FAMILY_03': 'null',
                    'PICK_BY_CODE': 'FIFO',
                    'ABC_CATEGORY': 'null',
                    'ABC_VALUE': '1',
                    'CBM_RATIO': '1',
                    'BOM_SKU': 'false',
                    'DEFAULT_EXPIRY': 'false',
                    'EXPIRY_FROM': 'null',
                    'EXPIRY_DAYS': 'null',
                    'EXPIRY_PERIOD': 'null',
                    'DEFAULT_MANF': 'null',
                    'MANUF_FROM': 'null',
                    'MANUF_DAYS': 'null',
                    'MANUF_PERIOD': 'null',
                    'LAST_CC_DATE': '2020-11-24',
                    'MIN_STOCK_QTY': '0',
                    'MAX_STOCK_QTY': '0',
                    'REQUIRE_SCAN_IN_SERIAL': 'null',
                    'REQUIRE_SCAN_OUT_SERIAL': 'null',
                    'SUSPEND_EDI_UPDATE': 'null',
                    'DEF_SCAN_IN_CONFIG_ID': 1,
                    'SKU_DEFINED_01': 'null',
                    'SKU_DEFINED_02': 'null',
                    'SKU_DEFINED_03': 'null',
                    'SKU_DEFINED_04': 'null',
                    'SKU_DEFINED_05': 'null',
                    'SKU_DEFINED_06': 'null',
                    'SKU_DEFINED_07': 'null',
                    'SKU_DEFINED_08': 'null',
                    'SKU_DEFINED_09': 'null',
                    'SKU_DEFINED_10': 'null',
                    "SKU_IMAGE_1": "",
                    'REMARKS': 'null',
                    'PUTAWAY_BY_CODE': 'null',
                    '1NYBT20RJ4WBXMOJEVA3': "qqq",
                    'DIMENSION': [
                        {
                            'SKU_LEVEL': '1',
                            'PACK_CODE': 'PCS',
                            'PACK_QTY': '3',
                            'DEF_PACK': 'true',
                            'LENGTH': '1.5',
                            'WIDTH': '1.5',
                            'HEIGHT': '1',
                            'LENGTH_UOM': 'CM',
                            'VOLUME': '1',
                            'VOLUME_UOM': 'CBM',
                            'NET_WEIGHT': '1',
                            'GROSS_WEIGHT': '1',
                            'WEIGHT_UOM': 'KG',
                            "PRICE": 1000,
                            "DISCOUNT_BY": 'PERCENT', # PERCENT, VALUE
                            "DISCOUNT_VALUE": 20,
                            "BARCODE": [
                                {
                                    "SKU_REF_CODE": "CCYX",
                                    "SKU_REF_TYPE": "A",
                                    "SKU_REF_BARCODE": "KA1"
                                }
                            ]
                        }
                    ],
                    'BOM': [
                        {
                            "QTY": 19,
                            "SKU_CHILD_CODE": "K113417000",
                        }
                    ]
                }
            ]
        }
    return SKU