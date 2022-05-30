class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        my_dict = {}
        for _ in range(len(senders)):
            if senders[_] in my_dict.keys():
                my_dict[senders[_]] += len(messages[_].split())
            else:
                my_dict[senders[_]] = len(messages[_].split())
        # print(my_dict)
        value = max(my_dict.values())
        # print(value)
        my_list = [k for k, v in my_dict.items() if v == value]
        # print(my_list)
        my_list.sort(key=lambda x: len(x), reverse=True)
        # print(my_list)
        my_list.sort(reverse=True)
        # print(my_list)
        return my_list[0]
