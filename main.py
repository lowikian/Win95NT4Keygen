import cd_key
import oem_key
import eleven_cd_key

if __name__ == "__main__":
    key_file = open("keys.txt", "w")
    
    print("Please wait while where generating keys")
    print("To exit press Ctrl + C")
    while True:
        try:
            #print("CD Key: " + cd_key.cd_keygen_first_segment() + '-' + cd_key.check_seven_digit())
            #print("OEM Key: " + oem_key.oem_first_segment() + '-OEM-' + oem_key.check_second_digit() + '-' + oem_key.oem_third_segment())
            #print("11-digit CD Key: " + eleven_cd_key.eleven_cd_keygen_first_segment() + '-' + eleven_cd_key.check_seven_digit())
            key_file.write("CD Key: " + cd_key.cd_keygen_first_segment() + '-' + cd_key.check_seven_digit() + '\n'
                       "OEM Key: " + oem_key.oem_first_segment() + '-OEM-' + oem_key.check_second_digit() + '-' + oem_key.oem_third_segment() + '\n'
                       "11-digit CD Key: " + eleven_cd_key.eleven_cd_keygen_first_segment() + '-' + eleven_cd_key.check_seven_digit() + '\n')
        except KeyboardInterrupt :
            break