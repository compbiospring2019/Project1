import dp_table
import utils

def main(): 
    #utils.read_sequence('')

    table = dp_table.DPTable('DAN', 'ANN')
    table.calculate_alignment()
    utils.print_table(table.table)
    
    print ("score:", table.score)
    utils.print_alignment(table.aligned1, table.aligned2)
if __name__ == "__main__":main()



