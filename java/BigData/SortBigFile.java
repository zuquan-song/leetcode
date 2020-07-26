package BigData;

import java.io.*;
import java.nio.file.Paths;
import java.util.*;

/**
 * This class aims to solve large data file which cannot fit into memory
 * @Reference https://www.roytuts.com/sort-large-file-using-java/
 * @Author Zuquan Song
 */
/**
 * Split large file into several sorted temp Files
 */
class FileSplitSortMergeUtil {
    private static final int MAX_FILE_SIZE = 10 * 1024 * 1024;

    private static File writeOut(List<String> lines, int counter) {
        File dir = Paths.get("tmp").toFile();
        if (!dir.exists()) {
            dir.mkdir();
        }

        File file = Paths.get("tmp", "file-" + counter + ".txt").toFile();
        try (BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(file)))) {
            for (String s : lines) {
                bw.write(s + "\n");
            }
            bw.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return file;
    }

    public static List<File> splitAndSortTempFiles(String fileName) {
        List<File> files = new ArrayList<>();
        File file = new File(fileName);
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;
            int accumulateSize = 0;
            int counter = 0;
            List<String> lines = new ArrayList<>();
            while ((line = br.readLine()) != null) {
                lines.add(line);
                accumulateSize += line.getBytes().length;
                if (accumulateSize >= MAX_FILE_SIZE) {
                    System.out.println("Begin sort: ");
                    lines.sort((a, b) -> Integer.parseInt(a) > Integer.parseInt(b) ? 1: -1);
                    System.out.println("Begin writeOut: ");
                    files.add(writeOut(lines, counter ++));
                    System.out.println("Finish writeOut: " + files.get(files.size() - 1).getAbsolutePath());
                    lines = new ArrayList<>();
                    accumulateSize = 0;
                }
            }
            if (lines.size() != 0) {
                lines.sort((a, b) -> Integer.parseInt(a) > Integer.parseInt(b) ? 1: -1);
                files.add(writeOut(lines, counter));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return files;
    }

    public static void sortFile(List<File> files) {
        TreeMap<Integer, BufferedReader> treeMap = new TreeMap<>((a, b) -> a > b ? 1: -1);
        try (BufferedWriter bw = new BufferedWriter(new FileWriter("sorted_number.txt"))) {
            for (int i = 0; i < files.size(); i ++) {
                BufferedReader br = new BufferedReader(new FileReader(files.get(i)));
                treeMap.put(Integer.parseInt(br.readLine()), br);
            }

            while (!treeMap.isEmpty()) {
                Map.Entry<Integer, BufferedReader> entry = treeMap.pollFirstEntry();
                bw.write(entry.getKey() + "\n");
                String line;
                if ((line = entry.getValue().readLine()) != null) {
                    treeMap.put(Integer.parseInt(line), entry.getValue());
                }
            }
            bw.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public static void main(String[] args) {
        List<File> files = splitAndSortTempFiles("random_number.txt");
        sortFile(files);
    }
}
