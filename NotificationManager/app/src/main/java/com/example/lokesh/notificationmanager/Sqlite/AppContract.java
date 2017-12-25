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


}
