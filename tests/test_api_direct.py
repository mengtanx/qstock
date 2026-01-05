#!/usr/bin/env python3
"""
直接测试同花顺API的周期参数
"""

import requests
import json

def test_api_direct():
    """直接测试不同周期的API调用"""

    print("直接测试同花顺API不同周期参数...")
    print("=" * 50)

    # 白酒概念的代码（从之前的分析中得知）
    symbol_code = "885611"
    year = "2024"

    # 测试不同周期
    periods = {
        '日线': '01',
        '周线': '11',
        '月线': '21'
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "Referer": "http://q.10jqka.com.cn",
        "Host": "d.10jqka.com.cn",
    }

    for period_name, period_code in periods.items():
        print(f"\n测试{period_name}数据...")

        url = f"http://d.10jqka.com.cn/v4/line/bk_{symbol_code}/{period_code}/{year}.js"

        try:
            print(f"请求URL: {url}")
            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code == 200:
                data_text = response.text

                # 检查是否包含有效数据
                if '{' in data_text and '}' in data_text:
                    try:
                        # 提取JSON部分
                        json_start = data_text.find('{')
                        json_end = data_text.rfind('}') + 1
                        json_data = data_text[json_start:json_end]

                        data = json.loads(json_data)

                        if 'data' in data and data['data']:
                            data_points = data['data'].split(';')
                            print(f"✅ {period_name}API响应成功")
                            print(f"   数据点数量: {len(data_points)}")
                            print(f"   第一个数据点: {data_points[0] if data_points else '无'}")
                        else:
                            print(f"❌ {period_name}数据格式异常")

                    except json.JSONDecodeError as e:
                        print(f"❌ {period_name}JSON解析失败: {e}")
                else:
                    print(f"❌ {period_name}响应不包含JSON数据")

            else:
                print(f"❌ {period_name}HTTP请求失败: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"❌ {period_name}网络请求异常: {e}")
        except Exception as e:
            print(f"❌ {period_name}其他异常: {e}")

    print("\n" + "=" * 50)
    print("API直接测试完成！")

if __name__ == "__main__":
    test_api_direct()
