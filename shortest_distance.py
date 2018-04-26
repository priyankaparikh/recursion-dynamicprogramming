# Leetcode 317:
# You want to build a house on an empty land which reaches all buildings in the shortest amount
# of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2,
# where:
    # Each 0 marks an empty land which you can pass by freely.
    # Each 1 marks a building which you cannot pass through.
    # Each 2 marks an obstacle which you cannot pass through.
# For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):
   # 1 - 0 - 2 - 0 - 1
   # |   |   |   |   |
   # 0 - 0 - 0 - 0 - 0
   # |   |   |   |   |
   # 0 - 0 - 1 - 0 - 0
   #
# The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is
# minimal. So return 7.
# code reference
# http://buttercola.blogspot.ca/2016/01/leetcode-shortest-distance-from-all.html
    # * Analysis from the above blog:
    # * Note:
    #    There will be at least one building. If it is not possible to build such house according to
    #    the above rules, return -1.
    #    Understand the problem:
    #    A BFS problem. Search from each building and calculate the distance to the building.
    # *  One thing to note is an empty land must be reachable by all buildings. To achieve this,
    # *  maintain an array of counters. Each time we reach a empty land from a building, increase the
    # *  counter. Finally, a reachable point must have the counter equaling to the number of buildings.
