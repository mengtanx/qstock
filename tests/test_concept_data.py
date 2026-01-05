#!/usr/bin/env python3
"""
测试修改后的 ths_concept_data 函数
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_ths_concept_data():
    """测试 ths_concept_data 函数的不同周期参数"""

    try:
        from data.industry import ths_concept_data
        import pandas as pd

        print("开始测试 ths_concept_data 函数...")

        # 测试参数验证
        print("\n1. 测试参数验证...")
        try:
            ths_concept_data('白酒概念', freq='invalid')
            print("❌ 参数验证失败：应该抛出 ValueError")
        except ValueError as e:
            print(f"✅ 参数验证通过：{e}")
        except Exception as e:
            print(f"❌ 参数验证出错：{e}")

        # 测试日线数据
        print("\n2. 测试日线数据获取...")
        try:
            df_d = ths_concept_data('白酒概念', start='2024', freq='d')
            print(f"✅ 日线数据获取成功")
            print(f"   数据形状: {df_d.shape}")
            print(f"   数据列数: {len(df_d.columns)}")
            if not df_d.empty:
                print(f"   最新日期: {df_d.index[-1] if hasattr(df_d.index, '__getitem__') else 'N/A'}")
        except Exception as e:
            print(f"❌ 日线数据获取失败: {e}")

        # 测试周线数据
        print("\n3. 测试周线数据获取...")
        try:
            df_w = ths_concept_data('白酒概念', start='2024', freq='w')
            print(f"✅ 周线数据获取成功")
            print(f"   数据形状: {df_w.shape}")
            print(f"   数据列数: {len(df_w.columns)}")
            if not df_w.empty:
                print(f"   最新日期: {df_w.index[-1] if hasattr(df_w.index, '__getitem__') else 'N/A'}")
        except Exception as e:
            print(f"❌ 周线数据获取失败: {e}")

        # 测试月线数据
        print("\n4. 测试月线数据获取...")
        try:
            df_m = ths_concept_data('白酒概念', start='2024', freq='m')
            print(f"✅ 月线数据获取成功")
            print(f"   数据形状: {df_m.shape}")
            print(f"   数据列数: {len(df_m.columns)}")
            if not df_m.empty:
                print(f"   最新日期: {df_m.index[-1] if hasattr(df_m.index, '__getitem__') else 'N/A'}")
        except Exception as e:
            print(f"❌ 月线数据获取失败: {e}")

        # 比较不同周期的数据量
        print("\n5. 比较不同周期数据...")
        try:
            if 'df_d' in locals() and 'df_w' in locals() and 'df_m' in locals():
                print(f"日线数据量: {len(df_d)}")
                print(f"周线数据量: {len(df_w)}")
                print(f"月线数据量: {len(df_m)}")

                # 验证周线数据量小于等于日线
                if len(df_w) <= len(df_d):
                    print("✅ 周线数据量验证通过")
                else:
                    print("❌ 周线数据量异常")

                # 验证月线数据量小于等于周线
                if len(df_m) <= len(df_w):
                    print("✅ 月线数据量验证通过")
                else:
                    print("❌ 月线数据量异常")
        except Exception as e:
            print(f"❌ 数据比较失败: {e}")

        print("\n测试完成！")

    except ImportError as e:
        print(f"❌ 导入失败: {e}")
        print("请确保所有依赖都已安装")
    except Exception as e:
        print(f"❌ 测试过程中出现未知错误: {e}")

if __name__ == "__main__":
    test_ths_concept_data()
