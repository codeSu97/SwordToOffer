# [剑指Offer 30. 包含main函数的栈](https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/)

## 题目内容

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

- 示例:

```shell
  MinStack minStack = new MinStack();
  minStack.push(-2);
  minStack.push(0);
  minStack.push(-3);
  minStack.min();   --> 返回 -3.
  minStack.pop();
  minStack.top();   --> 返回 0.
  minStack.min();   --> 返回 -2.
```

- 提示：
  - 各函数的调用总次数不超过 20000 次

## 解题思路

1. 空间换时间
2. 普通栈的push、pop、top操作都是O(1)，min()需要遍历所有元素，那么需要借助第二个栈来完成min()操作
3. 第二个栈`min_stack`从大到小存放数据，把`x`压入主栈`main_stack`的同时保证`min_stack`的栈顶一直是最小值：
   1. 若`min_stack`没有值，则把`x`压入`min_stack`
   2. 若`min_stack`有值且`x`小于等于`min_stack`的栈顶，则把`x`压入`min_stack`
4. min()函数取`min_stack`的栈顶
