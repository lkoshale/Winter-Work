package com.example.lokesh.notificationmanager;

import android.app.Notification;
import android.app.Service;
import android.content.Intent;
import android.graphics.drawable.Icon;
import android.os.IBinder;
import android.service.notification.NotificationListenerService;
import android.service.notification.StatusBarNotification;
import android.support.annotation.IntDef;
import android.util.Log;

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

        Log.e("Service:","New notification , "+sbn.getNotification().tickerText+" -- "+sbn.getPackageName());

    }

}


