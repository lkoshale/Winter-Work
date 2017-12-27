package com.example.lokesh.notificationmanager.Service;

import android.app.Notification;
import android.content.ContentValues;
import android.content.Intent;
import android.content.pm.ApplicationInfo;
import android.content.pm.PackageManager;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.graphics.drawable.Icon;
import android.os.IBinder;
import android.service.notification.NotificationListenerService;
import android.service.notification.StatusBarNotification;
import android.util.Log;

import com.example.lokesh.notificationmanager.Sqlite.AppContract;
import com.example.lokesh.notificationmanager.Sqlite.DBHelper;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by lokesh on 23/12/17.
 */

public class ListnerService extends NotificationListenerService {

    public ListnerService() {
        super();
        Log.e("Service","constructor");

    }

    @Override
    public int onStartCommand(Intent intent,int flags, int startId) {
        Log.e("Service","command");
        return super.onStartCommand(intent, flags, startId);
    }

    @Override
    public IBinder onBind(Intent intent) {
        return super.onBind(intent);
    }


    @Override
    public void onListenerConnected() {
        super.onListenerConnected();
        Log.e("service :","connected");
    }

    @Override
    public void onListenerDisconnected() {
        super.onListenerDisconnected();
        Log.e("Service:","disconnected");
    }


    @Override
    public void onNotificationPosted(StatusBarNotification sbn) {
        super.onNotificationPosted(sbn);
        Notification nf = sbn.getNotification();
//        Icon sm =  nf.getSmallIcon();

       // cancelNotification( sbn.getKey() );

        if(getPackageList().contains(sbn.getPackageName())){
            cancelNotification(sbn.getKey());
        }

        String str = sbn.getNotification().extras.getCharSequence(Notification.EXTRA_TEXT)+" *** "
                +sbn.getNotification().extras.getCharSequence(Notification.EXTRA_TITLE)+"***"+
                sbn.getNotification().extras.getCharSequence(Notification.EXTRA_TEXT_LINES)+"***"+
                sbn.getNotification().extras.getCharSequence(Notification.EXTRA_BIG_TEXT)+"***"+
                sbn.getNotification().extras.getCharSequence(Notification.EXTRA_SUB_TEXT)+"\n"+
                sbn.getNotification().extras.getCharSequence(Notification.EXTRA_INFO_TEXT)+"****"+
                sbn.getNotification().extras.getCharSequence(Notification.EXTRA_MESSAGES);


        DBHelper dbHelper = new DBHelper(getApplicationContext());
        SQLiteDatabase db = dbHelper.getWritableDatabase();

        PackageManager pm = getApplicationContext().getPackageManager();
        ApplicationInfo ai;
        try {
            ai = pm.getApplicationInfo( sbn.getPackageName(), 0);

        } catch (final PackageManager.NameNotFoundException e) {
            ai = null;
        }
        String appName = (String) pm.getApplicationLabel(ai);

        ContentValues contentValues = new ContentValues();
        contentValues.put(AppContract.TempTable.COLUMN_APP_NAME,appName);
        contentValues.put(AppContract.TempTable.COLUMN_PACKG,sbn.getPackageName());
        contentValues.put(AppContract.TempTable.COLUMNT_NOT_TEXT,str);

        db.insert(AppContract.TempTable.TABLE_NAME,null,contentValues);

        Log.e("Service: ","New notification , "+sbn.getNotification().tickerText+" -- "+sbn.getPackageName());
        Log.e("Service: ","new notification "+ str);

        db.close();
        dbHelper.close();

    }

    public List<String> getPackageList(){
        List<String>bList = new ArrayList<>();

        DBHelper dbHelper = new DBHelper(getApplicationContext());
        SQLiteDatabase db = dbHelper.getReadableDatabase();

        String rQuery = " SELECT * FROM "+ AppContract.BlockedAppTable.TABLE_NAME+" ";

        Cursor cursor = db.rawQuery(rQuery,null);

        while (cursor.moveToNext()){
            String packagename = cursor.getString(cursor.getColumnIndex(AppContract.BlockedAppTable.COLUMN_PACKAGE_NAME));
            bList.add(packagename);
        }

        cursor.close();
        db.close();
        dbHelper.close();
        return bList;
    }

}


