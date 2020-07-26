package amazon.ood;

import java.io.File;
import java.io.IOException;
import java.io.OutputStream;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static java.util.stream.Collectors.toList;

interface Command {
    void process();
}

interface FileFilter {
    boolean isSatisfied(File f);
}

abstract class OutputFormat {
    protected final OutputStream output;

    public OutputFormat(OutputStream output) {
        this.output = output;
    }

    abstract void outputResult(File file);
}

class ListFileCommand implements Command {
    private final String directory;
    private final ArrayList<FileFilter> filters;
    private final OutputFormat formatter;

    public ListFileCommand(String directory, ArrayList<FileFilter> filters, OutputFormat formatter) {
        this.directory = directory;
        this.filters = filters;
        this.formatter = formatter;
    }

    public ListFileCommand(String directory) {
        this(directory, new ArrayList<>(), new OutputFormat(System.out) {
            public void outputResult(File file) {
                ((PrintStream) this.output).printf("%s ", file.getName());
            }
        });
    }

    @Override
    public void process() {
        File file = new File(this.directory);
        List<File> listFiles = Arrays.asList(file.listFiles());
        for (FileFilter filter: this.filters)
            listFiles = listFiles.stream().filter(f -> filter.isSatisfied(f)).collect(toList());
        for (File f : listFiles) {
            this.formatter.outputResult(f);
        }
    }
}


public class CommandTest {
    public static void main(String[] args) throws IOException {
        OutputStream output = System.out;
        output.write("Hello world".getBytes());
        output.flush();
    }
}
