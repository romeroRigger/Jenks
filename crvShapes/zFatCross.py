import maya.cmds as cmds
#Settings Control
def create(n,suf):
    n=str(n+suf)
    c=[]
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\
                ],\
                point = [\
                            (-2.0, 0.0, -2.0),\
                            (-2.0, 0.0, -3.0),\
                            (2.0, 0.0, -3.0),\
                            (2.0, 0.0, -2.0),\
                            (3.0, 0.0, -2.0),\
                            (3.0, 0.0, 2.0),\
                            (2.0, 0.0, 2.0),\
                            (2.0, 0.0, 3.0),\
                            (-2.0, 0.0, 3.0),\
                            (-2.0, 0.0, 2.0),\
                            (-3.0, 0.0, 2.0),\
                            (-3.0, 0.0, -2.0),\
                            (-2.0, 0.0, -2.0)\
                ]\
              ))
    cmds.rename(c[0],n)
    c[0]=n
    return c