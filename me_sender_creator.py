# Main program that create parameter of a new user

import me_components_save, me_sender_creator_display


def main():
    COLLECTION_SIZE = 100
    NUM_ICONS_SENDER = 5
    POSITION_LIST_SIZE = 15

    # user id and name
    current_id = input("id del usuario: ")
    current_name = input("nombre del usuario: ")

    # create user
    current_sender = me_components_save.Sender(current_id, current_name)

    # create icons collection and assign random icons to user
    icons = me_components_save.Icons(COLLECTION_SIZE)
    current_sender.icons = icons.random_choose(NUM_ICONS_SENDER)

    # create the position-list and choose random cell
    position_list = me_components_save.PositionList(POSITION_LIST_SIZE, NUM_ICONS_SENDER)
    current_sender.cell = position_list.random_cell()

    # present the icons and positions to the user
    new_display = me_sender_creator_display.UserDisplay()
    new_display.show_icon_position(current_sender)

    # present the cell of the position-list to the user
    new_display.show_cell(current_sender)

    # save to user database
    current_sender.save_info()


if __name__ == "__main__":
    main()






