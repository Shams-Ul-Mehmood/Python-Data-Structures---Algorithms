my_List = [ 2 , 5 , 6 , 8 , 1 , 9 , 0 , 3 , 4 , 7 ]

def bubbleSortting( structure ):
    number = len( structure )
    for index in range( number - 1 ):
        for position in range( number - 1 - index ):
            if structure[ position ] > structure[ position + 1 ]:
                temperary_Value = structure[ position ]
                structure[ position ] = structure[ position + 1 ]
                structure[ position + 1 ] = temperary_Value
    return structure

print( my_List )
for location in range( 0 , len( my_List ) ):
    print( "my_List[",location,"] = ",my_List[ location ] )

print( bubbleSortting(  my_List ) )
for location in range( 0 , len( bubbleSortting( my_List ) ) ):
    print( "my_List[",location,"] = ",my_List[ location ] )