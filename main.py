def create_pyramid(rows):
    for i in range(rows):
        print("*"*(i+1))


print('Hi')
pyramid_rows = int(input('Insert the rows: '))
create_pyramid(pyramid_rows)
