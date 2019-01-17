import cozmo;

# Variation 4 group
# mudathirmahgoub
# mudathirmahgoub


def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("variation 4").wait_for_completed()

if __name__ == "__main__":
    cozmo.run_program(cozmo_program)
