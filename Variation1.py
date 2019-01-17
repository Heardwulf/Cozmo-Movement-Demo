import cozmo


def move_to_position_square(robot, x, y):

    # get the current position and rotation
    current_x, current_y, current_z, angle_z = robot.pose.position. x, robot.pose.position.y, robot.pose.position.z, robot.pose.rotation.angle_z

    robot.drive_straight(cozmo.util.distance_mm(x), cozmo.util.speed_mmps(150)).wait_for_completed()

    print("current position: ({0}, {1}, {2})".format(current_x, current_y, current_z))
    print("current angle_z : {0}".format(angle_z.degrees))
    print("new position    : ({0}, {1}, {2})".format(x, y, 0))

    if y > current_y:
        robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
    else:
        robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()

    robot.drive_straight(cozmo.util.distance_mm(y), cozmo.util.speed_mmps(150)).wait_for_completed()


def cozmo_program(robot: cozmo.robot.Robot):
    move_to_position_square(robot, 100, 100)


if __name__ == "__main__":
    cozmo.run_program(cozmo_program)

