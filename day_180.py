# Given a stack of N elements, interleave the first half of the stack
# with the second half reversed using only one other queue. This should be done in-place.
#
# Recall that you can only push or pop from a stack,
# and enqueue or dequeue from a queue.

from queue import Queue


def solution(stack, queue, index=1):
    for _ in range(len(stack) - index):
        que.put(stack.pop())

    while que.qsize():
        stk.append(que.get())

    if len(stack) - index > 1:
        solution(stack, queue, index + 1)