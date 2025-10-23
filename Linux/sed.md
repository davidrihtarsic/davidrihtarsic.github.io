# SED

- insert new line before the 1st line:

        sed '1 i This is nwe line' file_name

- add new line after 1st line:

        sed '1 a This is new line' file_nam

- add new line after search parameter:

        sed '/search_parameter/a This is new line' file_nam

- delete 1st line:

        sed '1d'

