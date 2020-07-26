package amazon;

import java.util.*;
import java.util.stream.Collectors;

public class TopNCompetitors {
    public static void main(String[] args) {
        List<String> competitors = new ArrayList<>();
        competitors.add("newshop");
        competitors.add("shopnow");
        competitors.add("afshion");
        competitors.add("fashionbeats");
        competitors.add("mymarket");
        competitors.add("tcellular");

        List<String> reviews = new ArrayList<>();
        reviews.add("newshop is a providing good services in the city, everyone; everyone should use newshop");
        reviews.add("best services by newshop");
        reviews.add("fashionbeats has great services in the city");
        reviews.add("I am proud to have fashionbeats");
        reviews.add("mymarket has fashionbeats awesome services");
        reviews.add("Thanks Newshop for the quick delivery");
        process(6,3,6, competitors, reviews).forEach(System.out::println);
    }


    private static List<String> process(int numCompetitors, int topNCompetitors, int numReviews, List<String> competitors, List<String> reviews) {
        Map<String, Integer> freqs = new HashMap<>();

        for (String review: reviews) {
            for (String comp: competitors) {
                String[] words = review.toLowerCase().split(" ");
                for (String word: words) {
                    if (word.equals(comp.toLowerCase())) {
                        int count = freqs.getOrDefault(comp, 0);
                        freqs.put(comp, count + 1);
                        break;
                    }
                }
            }
        }
        freqs.forEach((key, value) -> System.out.println(key + ":" + value));
        return freqs.entrySet().stream()
                .sorted((a, b) -> {
                    if (a.getValue().equals(b.getValue())) {
                        return a.getKey().compareTo(b.getKey());
                    } else {
                        return b.getValue() - a.getValue();
                    }
                })
                .limit(topNCompetitors)
                .map(Map.Entry::getKey)
                .collect(Collectors.toList());
    }
}
