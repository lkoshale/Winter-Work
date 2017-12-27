package com.example.lokesh.notificationmanager.Sqlite;

import android.provider.BaseColumns;

/**
 * Created by lokesh on 25/12/17.
 */

public class AppContract {



    private AppContract(){

    }

    public static final class BlockedAppTable {

        public static final String TABLE_NAME = "blocked_application";

        public static final String ID ="ID";

        public static final String COLUMN_PACKAGE_NAME = "packageName";

        public static final String COLUMN_APPNAME = "appName";

        public static String CREATE_TABLE = "CREATE TABLE "+TABLE_NAME+" ( "+
                                            ID+" INTEGER ,"+
                                            COLUMN_PACKAGE_NAME+" TEXT ,"+
                                            COLUMN_APPNAME+ " TEXT ,"+
                                            "PRIMARY KEY ( "+ID+") )";
    }

    public static final class TempTable {

        public static final String TABLE_NAME = "temp";

        public static final String ID= "ID";

        public static final String COLUMN_APP_NAME = "appName";

        public static final String COLUMN_PACKG = "package";

        public static final String COLUMNT_NOT_TEXT = "text";

        public static String CREATE_TABLE = "CREATE TABLE IF NOT EXISTS "+TABLE_NAME+" ( "+
                ID+" INTEGER ,"+
                COLUMN_APP_NAME+" TEXT ,"+
                COLUMN_PACKG+ " TEXT ,"+
                COLUMNT_NOT_TEXT+" TEXT,"+
                "PRIMARY KEY ( "+ID+") )";

    }


}
