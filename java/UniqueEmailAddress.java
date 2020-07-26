import java.util.HashSet;
import java.util.Set;

class UniqueEmailAddress {
    public int numUniqueEmails(String[] emails) {
        Set<String> addrs = new HashSet<>();
        for(int i = 0; i < emails.length; i ++) {
            String formatAddr = this.formatRawAddr(emails[i]);
            if (null != formatAddr) {
                addrs.add(formatAddr);
            }
        }
        // System.out.println(Arrays.toString(addrs.toArray()));
        return addrs.size();
    }
    
    public String formatRawAddr(String email) {
        StringBuilder sb = new StringBuilder();
        int i = 0;
        int domainIdx = email.indexOf('@');
        if (domainIdx == 0) {
            return null;
        }
        
        for (; i < email.length(); i ++) {
            char ch = email.charAt(i);
            if (ch == '.') {
                continue;
            } else if (ch == '+' || ch == '@') {
                break;
            } else {
                sb.append(email.charAt(i));
            }
        }
        
        sb.append(email.substring(domainIdx));
        return sb.toString();
    }    
}
