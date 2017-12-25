package com.example.lokesh.notificationmanager;

import android.app.Activity;
import android.app.NotificationManager;
import android.content.ContentResolver;
import android.content.Intent;
import android.content.pm.ApplicationInfo;
import android.content.pm.PackageInfo;
import android.content.pm.PackageManager;
import android.provider.Settings;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.app.NotificationCompat;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import java.util.List;

public class MainActivity extends AppCompatActivity {

    private Button notify;
    private Activity activity;
    private Button Listner;
    private Button stopService,appList;

    Intent serviceIntent;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        notify = (Button)findViewById(R.id.notify);
        Listner = (Button)findViewById(R.id.nListen);
        stopService =(Button)findViewById(R.id.stopService);
        appList = (Button)findViewById(R.id.appList);

        activity = this;



        notify.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                android.support.v4.app.NotificationCompat.Builder mBuilder =
                        new NotificationCompat.Builder(activity)
                                .setSmallIcon(R.mipmap.ic_launcher)
                                .setContentTitle("My notification")
                                .setContentText("Hello World!");
                // Sets an ID for the notification
                int mNotificationId = 001;
                // Gets an instance of the NotificationManager service
                NotificationManager mNotifyMgr = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
                // Builds the notification and issues it.
                mNotifyMgr.notify(mNotificationId, mBuilder.build());
            }
        });

        serviceIntent = new Intent(MainActivity.this,ListnerService.class);

        Listner.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startService(serviceIntent);
            }
        });


        stopService.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                stopService(serviceIntent);
                PackageManager pm = getPackageManager();
//get a list of installed apps.
                List<ApplicationInfo> packages = pm.getInstalledApplications(PackageManager.GET_META_DATA);

//                for (ApplicationInfo packageInfo : packages) {
//                    if(!isSystemPackage(packageInfo)) {
//                        Log.e("stop Button", "Installed package :" + packageInfo.packageName);
//                        Log.e("stop Button", "--name---- :" + getPackageManager().getApplicationLabel(packageInfo));
//                        Log.e("stop button", "Launch Activity :" + pm.getLaunchIntentForPackage(packageInfo.packageName));
//                    }
//                }

                startActivity(new Intent("android.settings.ACTION_NOTIFICATION_LISTENER_SETTINGS"));

                //Log.e("LISTNER RESP",String.valueOf(isNotificationServiceRunning()));

            }
        });

        appList.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(MainActivity.this,AppList.class);
                startActivity(i);
            }
        });

    }

    private boolean isSystemPackage(ApplicationInfo applicationInfo) {
        return ((applicationInfo.flags & ApplicationInfo.FLAG_SYSTEM) != 0) ? true
                : false;
    }


    //CHECK if notificationListnerservice iis enabled



}



