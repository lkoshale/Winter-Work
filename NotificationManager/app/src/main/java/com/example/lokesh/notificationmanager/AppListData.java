package com.example.lokesh.notificationmanager;

import android.graphics.drawable.Drawable;
import android.os.ParcelUuid;

/**
 * Created by lokesh on 24/12/17.
 */

public class AppListData {

    public String appName;
    public String packageName;
    public Drawable appIcon;

    public AppListData( String name,String packageName,Drawable icon){
        this.appIcon = icon;
        this.appName = name;
        this.packageName = packageName;
    }

}
