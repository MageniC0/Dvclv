print("[core]version:1.2.0/alpha.")
import laer.flu as flu
import laer.valley as vale
import laer.dimo as laer
print("[core]script dawn.")


def main():
    
    def boat():
        
        su = input("[core]exit?").lower()
        
        if su == "1":
            return()
        
        if su == "0":
            print("[core]done.")
            
            exit()
    
    print("[dvclv]live dustormn.")
    print("1_flu")
    print("2_vale")
    print("3_laer")
    
    inp = input("_")
    
    if inp == "1":
        
        print("[flu]live flu.")
        
        filename = input("name:")
        flu.manage_json(filename)
        
        boat()
    
    elif inp == "2":
        print("[vale]live vale.")
        
        vale.main()
        
        #
        boat()
    
    elif inp == "3":
        
        print("[303].ytilaer evil")
        
        tr_name = input("terrian map:")
        output_name = input("name:") + ".png"
        laer.g_map(tr_name, output_name)
        
        boat()
    
    else:
        print("???")

if __name__ == "__main__":
    main()