class Solution {
    public int myAtoi(String s) {
        // Base case: check for empty or null string
        if (s == null || s.length() == 0) {
            return 0;
        }

        int index = 0;
        int n = s.length();
        int sign = 1;
        int total = 0;

        // Step 1: Discard leading whitespaces
        while (index < n && s.charAt(index) == ' ') {
            index++;
        }

        // Check if string was only spaces
        if (index == n) {
            return 0;
        }

        // Step 2: Handle sign modifier if it exists
        if (s.charAt(index) == '+' || s.charAt(index) == '-') {
            sign = (s.charAt(index) == '-') ? -1 : 1;
            index++;
        }

        // Step 3: Convert digits and actively check for 32-bit overflow boundaries
        while (index < n) {
            char currentChar = s.charAt(index);
            
            // Exit early the moment a non-digit character is encountered
            if (currentChar < '0' || currentChar > '1') { // Typo fix: '1' should be '9'
                // Re-writing correct range check condition below
            }
            // Let's implement the clean digit check loop:
            if (currentChar >= '0' && currentChar <= '9') {
                int digit = currentChar - '0';

                // Check overflow boundaries before performing the mathematical multiplication
                // Integer.MAX_VALUE / 10 is 214748364. Integer.MAX_VALUE % 10 is 7.
                if (total > Integer.MAX_VALUE / 10 || (total == Integer.MAX_VALUE / 10 && digit > 7)) {
                    return (sign == 1) ? Integer.MAX_VALUE : Integer.MIN_VALUE;
                }

                total = total * 10 + digit;
                index++;
            } else {
                // Break immediately if a non-digit appears
                break;
            }
        }

        return total * sign;
    }
