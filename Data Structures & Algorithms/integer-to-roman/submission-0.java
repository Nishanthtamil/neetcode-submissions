class Solution {
    public String intToRoman(int num) {
        String[][] roman = {
            {"I","1"} , {"IV" ,"4"} ,{"V" ,"5"}, {"IX" ,"9"},
            {"X" ,"10"}, {"XL" ,"40"},{"L","50"},{"XC","90"},
            {"C","100"}, {"CD","400"} ,{"D","500"},{"CM","900"},
            {"M","1000"}
        };
        StringBuilder res = new StringBuilder();
        for (int i= roman.length -1 ; i>=0 ;i--){
            String rom = roman[i][0];
            int val = Integer.parseInt(roman[i][1]);
            int count = num / val;
            if (count>0){
                res.append(rom.repeat(count));
                num %=val;
            }
        }
        return res.toString();
    }
}