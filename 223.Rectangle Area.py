class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    class dot():
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class rectangle():
        def __init__(self, A, B, C, D):
            self.LeftBottom = Solution.dot(A,B)
            self.RightUp = Solution.dot(C,D)

    def commonArea(self, rec1, rec2):
        dx = min( rec1.RightUp.x, rec2.RightUp.x ) - max( rec1.LeftBottom.x, rec2.LeftBottom.x )
        dy = min( rec1.RightUp.y, rec2.RightUp.y ) - max( rec1.LeftBottom.y, rec2.LeftBottom.y )
        if dx <= 0 or dy <= 0:
            return 0
        return dx * dy

    def computeArea(self, A, B, C, D, E, F, G, H):
        a = Solution.rectangle(A,B,C,D)
        b = Solution.rectangle(E,F,G,H)
        area1 = self.commonArea(a, b)
        return (C-A)*(D-B) + (G-E)*(H-F) - area1







a = Solution()
print a.computeArea(-3, 0, 3, 4, 0, -1, 9, 2)
print a.computeArea(0, 0, 1, 1, 0, 0, 2, 2)