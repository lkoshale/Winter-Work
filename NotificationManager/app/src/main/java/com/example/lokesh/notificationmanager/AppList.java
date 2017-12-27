package com.example.lokesh.notificationmanager;

import android.content.ContentResolver;
import android.content.Intent;
import android.content.pm.ApplicationInfo;
import android.content.pm.PackageManager;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.provider.Settings;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.View;

import com.example.lokesh.notificationmanager.adapter.AppListAdapter;

import java.util.ArrayList;
import java.util.List;

public class AppList extends AppCompatActivity {

    private RecyclerView recyclerView;
    private RecyclerView.Adapter mAdapter;
    private RecyclerView.LayoutManager mLayoutManager;

    private List<AppListData> mList = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_app_list);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        if(!isNotificationServiceRunning()){
            startActivity(new Intent("android.settings.ACTION_NOTIFICATION_LISTENER_SETTINGS"));
        }

        setListData();


        recyclerView = (RecyclerView)findViewById(R.id.my_recycler_view);

        mLayoutManager = new LinearLayoutManager(this);
        recyclerView.setLayoutManager(mLayoutManager);

        mAdapter = new AppListAdapter(mList,this);
        recyclerView.setAdapter(mAdapter);

        getSupportActionBar().setDisplayHomeAsUpEnabled(true);
    }


    public void setListData(){

        PackageManager pm = getPackageManager();
        //get a list of installed apps.
        List<ApplicationInfo> packages = pm.getInstalledApplications(PackageManager.GET_META_DATA);

        for (ApplicationInfo packageInfo : packages) {

            if(!isSystemPackage(packageInfo)) {

                String name = (String)pm.getApplicationLabel(packageInfo);
                Drawable icon = pm.getApplicationIcon(packageInfo);
                AppListData data = new AppListData(name,packageInfo.packageName,icon);

                mList.add(data);
            }
        }

    }




    private boolean isSystemPackage(ApplicationInfo applicationInfo) {
        return ((applicationInfo.flags & ApplicationInfo.FLAG_SYSTEM) != 0) ? true
                : false;
    }


    @Override
    protected void onResume() {
        super.onResume();
        if(!isNotificationServiceRunning()){
            startActivity(new Intent("android.settings.ACTION_NOTIFICATION_LISTENER_SETTINGS"));
        }
    }

    public boolean isNotificationServiceRunning() {
        ContentResolver contentResolver = getContentResolver();

        String enabledNotificationListeners = Settings.Secure.getString(contentResolver, "enabled_notification_listeners");

        // Log.e("NOTFICATION LISTNER",enabledNotificationListeners);

        String packageName = getPackageName();
        return enabledNotificationListeners != null && enabledNotificationListeners.contains(packageName);
    }

}
