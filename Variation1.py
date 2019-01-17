import cozmo


def move_to_position_square(robot, x, y):

    # get the current position and rotation
    current_x, current_y, current_z = robot.pose.position. x, robot.pose.position.y, robot.pose.position.z
    angle_z = robot.pose.rotation.angle_z

    print("current position: ({0}, {1}, {2})".format(current_x, current_y, current_z))
    print("current angle_z : {0}".format(angle_z.degrees))
    print("new position    : ({0}, {1}, {2})".format(x, y, 0))

    waypoint_1 = cozmo.util.pose_z_angle(x, 0, 0, angle_z)

    robot.go_to_pose(waypoint_1, True).wait_for_completed()
    if y > current_y:
        angle_z = cozmo.util.degrees(angle_z.degrees + 90)
    else:
        angle_z = cozmo.util.degrees(angle_z.degrees - 90)

    waypoint_2 = cozmo.util.pose_z_angle(0, y, 0, angle_z)
    robot.go_to_pose(waypoint_2, True).wait_for_completed()


def cozmo_program(robot: cozmo.robot.Robot):
    move_to_position_square(robot, 100, -100)


if __name__ == "__main__":
    cozmo.run_program(cozmo_program)

