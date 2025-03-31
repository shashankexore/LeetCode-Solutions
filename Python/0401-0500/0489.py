class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def dfs(i, j, d):
            vis.add((i, j))
            robot.clean()
            for k in range(4):
                nd = (d + k) % 4
                x, y = i + dirs[nd], j + dirs[nd + 1]
                if (x, y) not in vis and robot.move():
                    dfs(x, y, nd)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                robot.turnRight()

        dirs = (-1, 0, 1, 0, -1)
        vis = set()
        dfs(0, 0, 0)
