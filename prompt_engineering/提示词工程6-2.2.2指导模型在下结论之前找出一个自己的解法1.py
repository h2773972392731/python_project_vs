from commonlibs import promptEngineering

# 在设计 Prompt 时，我们还可以通过明确指导语言模型进行自主思考，来获得更好的效果。 举个例子，假设我们要语言模型判断一个数学问题的解答是否正确。仅仅提供问题和解答是不够的，语 言模型可能会匆忙做出错误判断。
# 相反，我们可以在 Prompt 中先要求语言模型自己尝试解决这个问题，思考出自己的解法，然后再与提 供的解答进行对比，判断正确性。这种先让语言模型自主思考的方式，能帮助它更深入理解问题，做出 更准确的判断。
# 接下来我们会给出一个问题和一份来自学生的解答，要求模型判断解答是否正确：


prompt = f"""
判断学生的解决方案是否正确。
问题:
我正在建造一个太阳能发电站，需要帮助计算财务。
土地费用为 100美元/平方英尺
我可以以 250美元/平方英尺的价格购买太阳能电池板
我已经谈判好了维护合同，每年需要支付固定的10万美元，并额外支付每平方英尺10美元
作为平方英尺数的函数，首年运营的总费用是多少。
学生的解决方案：
设x为发电站的大小，单位为平方英尺。
费用：
土地费用：100x
太阳能电池板费用：250x
维护费用：100,000美元+100x
总费用：100x+250x+100,000美元+100x=450x+100,000美元
"""

response = promptEngineering.get_completion(prompt)
print(response)
