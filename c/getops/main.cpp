
#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <getopt.h>
#include <string>

#include "version.h"

using namespace std;


//---- version ----------------------------------------------------------------
#define STR_HELPER(x) #x
#define STR(x) STR_HELPER(x)

#define IS_BETA        1
#define VERSION_MAJOR  1
#define VERSION_MINOR  0
#define VERSION_BETA   1
#if IS_BETA
#define VERSION_FULL   "" STR(VERSION_MAJOR) "." STR(VERSION_MINOR) "." STR(VERSION_BETA) "-beta"
#else
#define VERSION_FULL   "" STR(VERSION_MAJOR) "." STR(VERSION_MINOR) "." STR(VERSION_BETA)
#endif
string version_full_str = VERSION_FULL;


//---- getopts ----------------------------------------------------------------
#define no_argument 0
#define required_argument 1 
#define optional_argument 2

struct arg_vals {
   std::string val_1;
   std::string val_2;
   std::string val_3;
};
arg_vals s_onearg_vals;
arg_vals s_twoarg_vals;
arg_vals s_threearg_vals;

bool verbose_on = false;
bool debug_on   = false;

/**********************************************************
 * @brief print command line options help message
 * 
 * @param app_name name to be print in message
 */
void print_usage(char* app_name) {
   printf("\n");
   printf("Version: %s\n", version_full_str.c_str());
   printf("Usage: %s.exe [option] [value] \n", app_name);
   printf("\n");
   printf("  -n, --noarg                          :No args\n");
   printf("  -1, --onearg=[VALUE]                 :One arg\n");
   printf("  -2, --twoarg=[VALUE,VALUE]           :Two args\n");
   printf("  -3, --threearg=[VALUE,VALUE,VALUE]   :Three args\n");
   printf("\n");
   printf("  -V, --verbose                        :Enable verbose\n");
   printf("  -D, --debug                          :Enable DEBUG\n");
   printf("\n");
   printf("  -v, --version                        :Show Version\n");
   printf("  -h, --help                           :Show Help menu\n");
   printf("\n");
}

// long options struct
const struct option longopts[] = {
   {"noarg",     no_argument,        0, 'n'},
   {"onearg",    required_argument,  0, '1'},
   {"twoarg",    required_argument,  0, '2'},
   {"threearg",  required_argument,  0, '3'},
   {"verbose",   no_argument,        0, 'V'},
   {"debug",     no_argument,        0, 'D'},
   {"version",   no_argument,        0, 'v'},
   {"help",      no_argument,        0, 'h'},
   {0,0,0,0},
};
// short argument string, args with values must have : after char
const char* single_args = "n1:2:3:VDvh";  // 


/**
 * @brief Parse passed argument value into <num> values
 *        split by <delim> and saved to <vals>
 * 
 * @param num           number of values to be split
 * @param delim         deliminator
 * @param optarg_value  value gotten from command line
 * @param vals          pointer to structure for split values
 * @return void
 */
void parse_optarg (int num, string delim, char* optarg_value, arg_vals *vals) {
   if (num < 2) return;
   string optarg_value_str = optarg_value;
   string delimiter = delim;  //string delimiter = ",";
   size_t pos = 0;
   string token;
   for (int i=1;i<=num;i++) {
      if (i < num){
         pos = optarg_value_str.find(delimiter);
         token = optarg_value_str.substr(0, pos);
         optarg_value_str.erase(0, pos + delimiter.length());
         if (i == 1) {vals->val_1 = token;}
         else if (i == 2) {vals->val_2 = token;}
         //std::cout << "token=" << token << std::endl;
      } else {
         if (i == 2) {vals->val_2 = token;}
         else if (i == 3) {vals->val_3 = optarg_value_str;}
         //std::cout << "s=" << optarg_value_str << std::endl;
      }
   }
}


/**
 * @brief get and process command line arguments
 * 
 * @param argc  passed directly from main()'s arg
 * @param argv  passed directly from main()'s arg
 * @return void
 */
void process_args (int argc, char * argv[]) {
   int index;
   while(true) {
      int iarg = getopt_long(argc, argv, single_args, longopts, &index);
      // if args are present, break on no args left to process
      if (argc > 1) if (iarg == -1) break;;
      char* optarg_value = optarg;
      switch (iarg) {
         case '1':
            s_onearg_vals.val_1 = optarg;
            break;
         case '2':
            parse_optarg(2, ",", optarg_value, &s_twoarg_vals);
            break;
         case '3':
            parse_optarg(3, ",", optarg_value, &s_threearg_vals);
            break;
         case 'v':
            cout << "Application Version: v" << version_full_str << endl;
            break;
         case 'V':
            verbose_on = true;
            break;
         case 'D':
            debug_on = true;
            break;
         case 'h':
         default: 
            print_usage(argv[0]); 
            exit(EXIT_FAILURE);
      }
   }
}

/**
 * @brief MAIN Function
 * 
 * @param argc 
 * @param argv 
 * @return int 
 */
int main(int argc, char * argv[]) {
   int status = 0;
   
   process_args(argc,argv);

   #if 1
      cout << "s_onearg_vals.val_1=" << s_onearg_vals.val_1 << endl;
      cout << "s_twoarg_vals.val_1=" << s_twoarg_vals.val_1 << endl;
      cout << "s_twoarg_vals.val_2=" << s_twoarg_vals.val_2 << endl;
      cout << "s_threearg_vals.val_1=" << s_threearg_vals.val_1 << endl;
      cout << "s_threearg_vals.val_2=" << s_threearg_vals.val_2 << endl;
      cout << "s_threearg_vals.val_3=" << s_threearg_vals.val_3 << endl;
      cout << "Debug = " << boolalpha << debug_on << endl;
      cout << "Verbose = " << boolalpha << verbose_on << endl;
   #endif
   

   return status; 
}