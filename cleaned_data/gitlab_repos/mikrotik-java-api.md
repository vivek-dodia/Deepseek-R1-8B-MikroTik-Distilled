# Repository Information
Name: mikrotik-java-api

# Files

File: config
================================================
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://gitlab.com/lsoimpe/mikrotik-java-api.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: grammar.txt
================================================
command  = action [ query ] [ return ]
action   = ("/" word)+
query    = "where" expr
expr     = expr "and" expr | expr "or" expr | "not" expr | hasExpr | eqExpr | lessExpr | moreExpr | notExpr
hasExpr  = name
eqExpr   = name "=" value
lessExpr = name "<" value
moreExpr = name ">" value
notExpr  = name "!=" value
return   = "return" (name)+
================================================

File: ApiConnection.java
================================================
package me.legrange.mikrotik;
import java.util.List;
import java.util.Map;
import javax.net.SocketFactory;
import me.legrange.mikrotik.impl.ApiConnectionImpl;
/**
 * The Mikrotik API connection. This is the class used to connect to a remote
 * Mikrotik and send commands to it.
 *
 * @author GideonLeGrange
 */
public abstract class ApiConnection implements AutoCloseable {
    /**
     * default TCP port used by Mikrotik API
     */
    public static final int DEFAULT_PORT = 8728;
    /**
     * default TCP TLS port used by Mikrotik API
     */
    public static final int DEFAULT_TLS_PORT = 8729;
    /**
     * default connection timeout to use when opening the connection
     */
    public static final int DEFAULT_CONNECTION_TIMEOUT = 60000;
    /**
     * default command timeout used for synchronous commands
     */
    public static final int DEFAULT_COMMAND_TIMEOUT = 60000;
    /**
     * Create a new API connection to the give device on the supplied port using 
     * the supplied socket factory to create the socket. 
     *
     * @param fact SocketFactory to use for TCP socket creation.
     * @param host The host to which to connect.
     * @param port The TCP port to use.
     * @param timeout The connection timeout to use when opening the connection.
     * @return The ApiConnection
     * @throws me.legrange.mikrotik.MikrotikApiException Thrown if there is a
     * problem connecting
     * @since 3.0
     */
    public static ApiConnection connect(SocketFactory fact, String host, int port, int timeout) throws MikrotikApiException {
        return ApiConnectionImpl.connect(fact, host, port, timeout);
    }
    /**
     * Create a new API connection to the give device on the default API port.
     *
     * @param host The host to which to connect.
     * @return The ApiConnection
     * @throws me.legrange.mikrotik.MikrotikApiException Thrown if there is a
     * problem connecting
     */
    public static ApiConnection connect(String host) throws MikrotikApiException {
        return connect(SocketFactory.getDefault(), host, DEFAULT_PORT, DEFAULT_COMMAND_TIMEOUT);
    }
    /**
     * Check the state of connection.
     *
     * @return if connection is established to router it returns true.
     */
    public abstract boolean isConnected();
    /**
     * Log in to the remote router.
     *
     * @param username - username of the user on the router
     * @param password - password for the user
     * @throws me.legrange.mikrotik.MikrotikApiException Thrown if the API encounters an error on login.
     */
    public abstract void login(String username, String password) throws MikrotikApiException;
    /**
     * execute a command and return a list of results.
     *
     * @param cmd Command to execute
     * @return The list of results
     * @throws me.legrange.mikrotik.MikrotikApiException Thrown if the API encounters an error executing a command.
     */
    public abstract List<Map<String, String>> execute(String cmd) throws MikrotikApiException;
    /**
     * execute a command and attach a result listener to receive it's results.
     *
     * @param cmd Command to execute
     * @param lis ResultListener that will receive the results
     * @return A command object that can be used to cancel the command.
     * @throws me.legrange.mikrotik.MikrotikApiException Thrown if the API encounters an error executing a command.
     */
    public abstract String execute(String cmd, ResultListener lis) throws MikrotikApiException;
    /**
     * cancel a command
     *
     * @param tag The tag of the command to cancel
     * @throws me.legrange.mikrotik.MikrotikApiException Thrown if there is a
     * problem cancelling the command
     */
    public abstract void cancel(String tag) throws MikrotikApiException;
    /**
     * set the command timeout. The command timeout is used to time out API
     * commands after a specific time.
     *
     * Note: This is not the same as the timeout value passed in the connect()
     * methods. This timeout is specific to synchronous
     * commands, that timeout is applied to opening the API socket.
     *
     * @param timeout The time out in milliseconds.
     * @throws MikrotikApiException Thrown if the timeout specified is invalid.
     * @since 2.1
     */
    public abstract void setTimeout(int timeout) throws MikrotikApiException;
    /**
     * Disconnect from the remote API
     *
     * @throws me.legrange.mikrotik.ApiConnectionException Thrown if there is a
     * problem closing the connection.
     * @since 2.2
     */
    @Override
    public abstract void close() throws ApiConnectionException;
}
================================================

File: ApiConnectionException.java
================================================
package me.legrange.mikrotik;
/**
 * Exception thrown if the Api experiences a connection problem
 * @author GideonLeGrange
 */
public class ApiConnectionException extends MikrotikApiException {
    /** 
     * Create a new exception. 
     * 
     * @param msg The message
     */
    public ApiConnectionException(String msg) {
        super(msg);
    }
    /** 
     * Create a new exception 
     * @param msg The message
     * @param err The underlying cause 
     */
    public ApiConnectionException(String msg, Throwable err) {
        super(msg, err);
    }
}
================================================

File: grammar.txt
================================================
command  = action [ query ] [ return ]
action   = ("/" word)+
query    = "where" expr
expr     = expr "and" expr | expr "or" expr | "not" expr | hasExpr | eqExpr | lessExpr | moreExpr | notExpr
hasExpr  = name
eqExpr   = name "=" value
lessExpr = name "<" value
moreExpr = name ">" value
notExpr  = name "!=" value
return   = "return" (name)+
================================================

File: ApiCommandException.java
================================================
package me.legrange.mikrotik.impl;
import me.legrange.mikrotik.MikrotikApiException;
/**
 * Thrown when the Mikrotik returns an error when receiving our command.
 * @author GideonLeGrange
 */
public class ApiCommandException extends MikrotikApiException {
    /** return the tag associated with this exception, if there is one
     * @return the tag associated with this exception. Null if there is no tag*/
    public String getTag() {
        return tag;
    }
     ApiCommandException(String msg) {
        super(msg);
    }
     ApiCommandException(String msg, Throwable err) {
        super(msg, err);
    }
    ApiCommandException(Error err) {
        super(err.getMessage());
        tag = err.getTag();
    }
    private String tag = null;
}
================================================

File: ApiConnectionImpl.java
================================================
package me.legrange.mikrotik.impl;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.LinkedBlockingQueue;
import javax.net.SocketFactory;
import me.legrange.mikrotik.ApiConnection;
import me.legrange.mikrotik.ApiConnectionException;
import me.legrange.mikrotik.MikrotikApiException;
import me.legrange.mikrotik.ResultListener;
/**
 * The Mikrotik API connection implementation. This is the class used to connect
 * to a remote Mikrotik and send commands to it.
 *
 * @author GideonLeGrange
 */
public final class ApiConnectionImpl extends ApiConnection {
    /**
     * Create a new API connection to the give device on the supplied port
     *
     * @param fact The socket factory used to construct the connection socket.
     * @param host The host to which to connect.
     * @param port The TCP port to use.
     * @param timeOut The connection timeout
     * @return The ApiConnection
     * @throws me.legrange.mikrotik.ApiConnectionException Thrown if there is a
     * problem connecting
     */
    public static ApiConnection connect(SocketFactory fact, String host, int port, int timeOut) throws ApiConnectionException {
        ApiConnectionImpl con = new ApiConnectionImpl();
        con.open(host, port, fact, timeOut);
        return con;
    }
    @Override
    public boolean isConnected() {
        return connected;
    }
    @Override
    public void login(String username, String password) throws MikrotikApiException {
        if (username.trim().isEmpty()) {
            throw new ApiConnectionException("API username cannot be empty");
        }
        List<Map<String, String>> list = execute("/login");
        Map<String, String> res = list.get(0);
        String hash = res.get("ret");
        String chal = Util.hexStrToStr("00") + new String(password.toCharArray()) + Util.hexStrToStr(hash);
        chal = Util.hashMD5(chal);
        execute("/login name=" + username + " response=00" + chal);
    }
    @Override
    public List<Map<String, String>> execute(String cmd) throws MikrotikApiException {
        return execute(Parser.parse(cmd), timeout);
    }
    @Override
    public String execute(String cmd, ResultListener lis) throws MikrotikApiException {
        return execute(Parser.parse(cmd), lis);
    }
    @Override
    public void cancel(String tag) throws MikrotikApiException {
        execute(String.format("/cancel tag=%s", tag));
    }
    @Override
    public void setTimeout(int timeout) throws MikrotikApiException {
        if (timeout > 0) {
            this.timeout = timeout;
        } else {
            throw new MikrotikApiException(String.format("Invalid timeout value '%d'; must be postive", timeout));
        }
    }
    @Override
    public void close() throws ApiConnectionException {
        if (!connected) {
            throw new ApiConnectionException(("Not/no longer connected to remote Mikrotik"));
        }
        connected = false;
        processor.interrupt();
        reader.interrupt();
        try {
            in.close();
            out.close();
            sock.close();
        } catch (IOException ex) {
            throw new ApiConnectionException(String.format("Error closing socket: %s", ex.getMessage()), ex);
        }
    }
    private List<Map<String, String>> execute(Command cmd, int timeout) throws MikrotikApiException {
        SyncListener l = new SyncListener();
        execute(cmd, l);
        return l.getResults(timeout);
    }
    private String execute(Command cmd, ResultListener lis) throws MikrotikApiException {
        String tag = nextTag();
        cmd.setTag(tag);
        listeners.put(tag, lis);
        try {
            Util.write(cmd, out);
        } catch (UnsupportedEncodingException ex) {
            throw new ApiDataException(ex.getMessage(), ex);
        } catch (IOException ex) {
            throw new ApiConnectionException(ex.getMessage(), ex);
        }
        return tag;
    }
    private ApiConnectionImpl() {
        this.listeners = new ConcurrentHashMap<>();
    }
    /**
     * Start the API. Connects to the Mikrotik
     */
    private void open(String host, int port, SocketFactory fact, int conTimeout) throws ApiConnectionException {
        try {
            InetAddress ia = InetAddress.getByName(host.trim());
            sock = fact.createSocket();
            sock.connect(new InetSocketAddress(ia, port), conTimeout);
            in = new DataInputStream(sock.getInputStream());
            out = new DataOutputStream(sock.getOutputStream());
            connected = true;
            reader = new Reader();
            reader.setDaemon(true);
            reader.start();
            processor = new Processor();
            processor.setDaemon(true);
            processor.start();
        } catch (UnknownHostException ex) {
            connected = false;
            throw new ApiConnectionException(String.format("Unknown host '%s'", host), ex);
        } catch (IOException ex) {
            connected = false;
            throw new ApiConnectionException(String.format("Error connecting to %s:%d : %s", host, port, ex.getMessage()), ex);
        }
    }
    private synchronized String nextTag() {
        _tag++;
        return Integer.toHexString(_tag);
    }
    private Socket sock = null;
    private DataOutputStream out = null;
    private DataInputStream in = null;
    private boolean connected = false;
    private Reader reader;
    private Processor processor;
    private final Map<String, ResultListener> listeners;
    private Integer _tag = 0;
    private int timeout = ApiConnection.DEFAULT_COMMAND_TIMEOUT;
    /**
     * thread to read data from the socket and process it into Strings
     */
    private class Reader extends Thread {
        private Reader() {
            super("Mikrotik API Reader");
        }
        private String take() throws ApiConnectionException, ApiDataException {
            Object val = null;
            try {
                val = queue.take();
            } catch (InterruptedException ex) {
                throw new ApiConnectionException("Interrupted while reading data from queue.", ex);
            }
            if (val instanceof ApiConnectionException) {
                throw (ApiConnectionException) val;
            } else if (val instanceof ApiDataException) {
                throw (ApiDataException) val;
            }
            return (String) val;
        }
        private boolean isEmpty() {
            return queue.isEmpty();
        }
        @Override
        public void run() {
            while (connected) {
                try {
                    String s = Util.decode(in);
                    put(s);
                } catch (ApiDataException ex) {
                    put(ex);
                } catch (ApiConnectionException ex) {
                    if (connected || !sock.isClosed()) {
                        put(ex);
                    }
                }
            }
        }
        private void put(Object data) {
            try {
                queue.put(data);
            } catch (InterruptedException ex) {
            }
        }
        private final LinkedBlockingQueue queue = new LinkedBlockingQueue(40);
    }
    /**
     * Thread to take the received strings and process it into Result objects
     */
    private class Processor extends Thread {
        private Processor() {
            super("Mikrotik API Result Processor");
        }
        @Override
        public void run() {
            while (connected) {
                Response res;
                try {
                    res = unpack();
                } catch (ApiCommandException ex) {
                    String tag = ex.getTag();
                    if (tag != null) {
                        res = new Error(tag, ex.getMessage());
                    } else {
                        continue;
                    }
                } catch (MikrotikApiException ex) {
                    continue;
                }
                ResultListener l = listeners.get(res.getTag());
                if (l != null) {
                    if (res instanceof Result) {
                        l.receive((Result) res);
                    } else if (res instanceof Done) {
                        if (l instanceof SyncListener) {
                            ((SyncListener) l).completed((Done) res);
                        } else {
                            l.completed();
                        }
                        listeners.remove(res.getTag());
                    } else if (res instanceof Error) {
                        l.error(new ApiCommandException((Error) res));
                    }
                }
            }
        }
        private void nextLine() throws ApiConnectionException, ApiDataException {
            if (lines.isEmpty()) {
                String block = reader.take();
                String parts[] = block.split("\n");
                lines.addAll(Arrays.asList(parts));
            }
            line = lines.remove(0);
        }
        private boolean hasNextLine() {
            return !lines.isEmpty() || !reader.isEmpty();
        }
        private String peekLine() throws ApiConnectionException, ApiDataException {
            if (lines.isEmpty()) {
                String block = reader.take();
                String parts[] = block.split("\n");
                lines.addAll(Arrays.asList(parts));
            }
            return lines.get(0);
        }
        private Response unpack() throws MikrotikApiException {
            if (line == null) {
                nextLine();
            }
            switch (line) {
                case "!re":
                    return unpackRe();
                case "!done":
                    return unpackDone();
                case "!trap":
                    return unpackError();
                case "!halt":
                    return unpackError();
                case "":
                default:
                    throw new ApiDataException(String.format("Unexpected line '%s'", line));
            }
        }
        private Result unpackRe() throws ApiDataException, ApiConnectionException {
            nextLine();
            int l = 0;
            Result res = new Result();
            while (!line.startsWith(("!"))) {
                l++;
                if (line.startsWith(("="))) {
                    String parts[] = line.split("=", 3);
                    if (parts.length == 3) {
                        if (!parts[2].endsWith("\r")) {
                            res.put(parts[1], unpackResult(parts[2]));
                        } else {
                            final StringBuilder sb = new StringBuilder();
                            sb.append(parts[2]);
                            while (!lines.isEmpty()) {
                                nextLine();
                                sb.append(line);
                            }
                            res.put(parts[1], sb.toString());
                        }
                    } else {
                        throw new ApiDataException(String.format("Malformed line '%s'", line));
                    }
                } else if (line.startsWith(".tag=")) {
                    String parts[] = line.split("=", 2);
                    if (parts.length == 2) {
                        res.setTag(parts[1]);
                    }
                } else {
                    throw new ApiDataException(String.format("Unexpected line '%s'", line));
                }
                if (hasNextLine()) {
                    nextLine();
                } else {
                    line = null;
                    break;
                }
            }
            return res;
        }
        private String unpackResult(String first) throws ApiConnectionException, ApiDataException {
            StringBuilder buf = new StringBuilder(first);
            line = null;
            while (hasNextLine()) {
                String peek = peekLine();
                if (!(peek.startsWith("!") || peek.startsWith("=") || peek.startsWith(".tag="))) {
                    nextLine();
                    buf.append("\n");
                    buf.append(line);
                } else {
                    break;
                }
            }
            return buf.toString();
        }
        private Done unpackDone() throws MikrotikApiException {
            Done done = new Done(null);
            if (hasNextLine()) {
                nextLine();
                while (!line.startsWith("!")) {
                    if (line.startsWith(".tag=")) {
                        String parts[] = line.split("=", 2);
                        if (parts.length == 2) {
                            done.setTag(parts[1]);
                        }
                    } else if (line.startsWith(("=ret"))) {
                        String parts[] = line.split("=", 3);
                        if (parts.length == 3) {
                            done.setHash(parts[2]);
                        } else {
                            throw new ApiDataException(String.format("Malformed line '%s'", line));
                        }
                    }
                    if (hasNextLine()) {
                        nextLine();
                    } else {
                        line = null;
                        break;
                    }
                }
            }
            return done;
        }
        private Error unpackError() throws MikrotikApiException {
            nextLine();
            Error err = new Error();
            if (hasNextLine()) {
                while (!line.startsWith("!")) {
                    if (line.startsWith(".tag=")) {
                        String parts[] = line.split("=", 2);
                        if (parts.length == 2) {
                            err.setTag(parts[1]);
                        }
                    } else if (line.startsWith("=message=")) {
                        err.setMessage(line.split("=", 3)[2]);
                    }
                    if (hasNextLine()) {
                        nextLine();
                    } else {
                        line = null;
                        break;
                    }
                }
            }
            return err;
        }
        private final List<String> lines = new LinkedList<>();
        private String line;
    }
    private static class SyncListener implements ResultListener {
        @Override
        public synchronized void error(MikrotikApiException ex) {
            this.err = ex;
            notifyAll();
        }
        @Override
        public synchronized void completed() {
            complete = true;
            notifyAll();
        }
        synchronized void completed(Done done) {
            if (done.getHash() != null) {
                Result res = new Result();
                res.put("ret", done.getHash());
                results.add(res);
            }
            complete = true;
            notifyAll();
        }
        @Override
        public void receive(Map<String, String> result) {
            results.add(result);
        }
        private List<Map<String, String>> getResults(int timeout) throws MikrotikApiException {
            try {
                synchronized (this) { // don't wait if we already have a result.
                    int waitTime = timeout;
                    while (!complete && (waitTime > 0)) {
                        long start = System.currentTimeMillis();
                        wait(waitTime);
                        waitTime = waitTime - (int) (System.currentTimeMillis() - start);
                        if ((waitTime <= 0) && !complete) {
                            err = new ApiConnectionException(String.format("Command timed out after %d ms", timeout));
                        }
                    }
                }
            } catch (InterruptedException ex) {
                throw new ApiConnectionException(ex.getMessage(), ex);
            }
            if (err != null) {
                throw new MikrotikApiException(err.getMessage(), err);
            }
            return results;
        }
        private final List<Map<String, String>> results = new LinkedList<>();
        private MikrotikApiException err;
        private boolean complete = false;
    }
}
================================================

File: ApiDataException.java
================================================
package me.legrange.mikrotik.impl;
import me.legrange.mikrotik.MikrotikApiException;
/**
 * Thrown if there is a problem unpacking data from the Api. 
 * @author GideonLeGrange
 */
public class ApiDataException extends MikrotikApiException {
    ApiDataException(String msg) {
        super(msg);
    }
    ApiDataException(String msg, Throwable err) {
        super(msg, err);
    }
}
================================================

File: MikrotikApiException.java
================================================
package me.legrange.mikrotik;
/**
 * Thrown by the Mikrotik API to indicate errors
 *
 * @author GideonLeGrange
 */
public class MikrotikApiException extends Exception {
    /** 
     * Create a new exception 
     * @param msg The message
     */
    public MikrotikApiException(String msg) {
        super(msg);
    }
    /** 
     * Create a new exception 
     * @param msg The message
     * @param err The underlying cause 
     */
    public MikrotikApiException(String msg, Throwable err) {
        super(msg, err);
    }
}
================================================

File: MikrotikJava.java
================================================
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mikrotik.java;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.net.ssl.SSLSocketFactory;
import me.legrange.mikrotik.*;
/**
 *
 * @author borex
 */
public class MikrotikJava {
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws MikrotikApiException {
        // TODO code application logic here
        mainw main = new mainw();
        main.jButton2.addMouseListener(new java.awt.event.MouseAdapter() {
             public void mouseClicked(java.awt.event.MouseEvent evt) {
                 try {
                     jButton2MouseClicked(evt);
                 } catch (MikrotikApiException ex) {
                     Logger.getLogger(MikrotikJava.class.getName()).log(Level.SEVERE, null, ex);
                 }
            }
            private void jButton2MouseClicked(java.awt.event.MouseEvent evt) throws MikrotikApiException {                                      
                // TODO add your handling code here:
        ApiConnection con = ApiConnection.connect("192.168.122.2"); // connect to router on the default API port and fail in 2 seconds
        con.login("admin","1"); // log in to router
        con.execute("/system/shutdown"); // execute a command
        con.close(); // disconnect from router
            } 
        });
        main.setVisible(true);
    }
}