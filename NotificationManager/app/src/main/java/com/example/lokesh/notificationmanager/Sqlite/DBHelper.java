package com.example.lokesh.notificationmanager.Sqlite;

import android.content.Context;
import android.database.Cursor;
import android.database.DatabaseErrorHandler;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.provider.Settings;
import android.util.Log;

import com.example.lokesh.notificationmanager.Sqlite.AppContract.BlockedAppTable;

/**
 * Created by lokesh on 25/12/17.
 */

public class DBHelper extends SQLiteOpenHelper {

    public static final String DATABASE_NAME = "NBlockedApps";
    public static final int DATABASE_VERSION = 1;

    public DBHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }


    @Override
    public void onCreate(SQLiteDatabase db) {

        //crete blocked app table
        db.execSQL(" DROP TABLE IF EXISTS "+ BlockedAppTable.TABLE_NAME);
        db.execSQL(BlockedAppTable.CREATE_TABLE);

    }

    @Override
    public void onUpgrade(SQLiteDatabase sqLiteDatabase, int i, int i1) {
        //do nothing
    }


    public void PrintTable(String TableName){
        SQLiteDatabase db = this.getReadableDatabase();
        String readQuery = " SELECT * FROM "+TableName+" ";
        Cursor cursor = db.rawQuery(readQuery,null);

        String tablestr = " TABLE : "+TableName+" \n";

        String[] columnNames = cursor.getColumnNames();

        while (cursor.moveToNext()){

            for (String col : columnNames){
                String val = cursor.getString(cursor.getColumnIndexOrThrow(col));
                tablestr+=" "+val+"\t";
            }
            tablestr+="\n";
        }

        Log.e("PrintTable ",tablestr);
    }

}
