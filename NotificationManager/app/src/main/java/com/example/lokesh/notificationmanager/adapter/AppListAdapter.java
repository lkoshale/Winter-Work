package com.example.lokesh.notificationmanager.adapter;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.Switch;
import android.widget.TextView;

import com.example.lokesh.notificationmanager.AppList;
import com.example.lokesh.notificationmanager.AppListData;
import com.example.lokesh.notificationmanager.R;
import com.example.lokesh.notificationmanager.Sqlite.AppContract;
import com.example.lokesh.notificationmanager.Sqlite.DBHelper;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by lokesh on 24/12/17.
 */

public class AppListAdapter extends RecyclerView.Adapter<AppListAdapter.ViewHolder> {

    private List<AppListData> mList;
    private Context context;
    private List<String>bList;

    public static class ViewHolder extends RecyclerView.ViewHolder {

        private TextView nameView;
        private Switch onOFF;
        private ImageView iconView;


        public ViewHolder(View itemView) {
            super(itemView);
            nameView= (TextView)itemView.findViewById(R.id.recylerview_name);
            onOFF = (Switch)itemView.findViewById(R.id.recyclerview_switch);
            iconView = (ImageView)itemView.findViewById(R.id.recyclerview_appicon);
        }
    }

    public AppListAdapter(List<AppListData> mList, Context context){
        this.context = context;
        this.bList = getBlockedPackageList();
        this.mList = setONitemFirst(mList);


    }

    @Override
    public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View itemView = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.layout_app_list, parent, false);

        return new ViewHolder(itemView);
    }

    @Override
    public void onBindViewHolder(ViewHolder holder, int position) {

        final AppListData data = mList.get(position);
        holder.nameView.setText(data.appName);
        holder.iconView.setImageDrawable(data.appIcon);

        if(this.bList.contains(data.packageName)){
            holder.onOFF.setChecked(true);
           // Log.e("ON",data.packageName);
        }else{
            holder.onOFF.setChecked(false);
        }

        final ViewHolder holder1 = holder;

            holder.onOFF.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {

                    DBHelper db_handle = new DBHelper(context);
                    SQLiteDatabase db = db_handle.getWritableDatabase();
                    String Query = " SELECT * FROM "+ AppContract.BlockedAppTable.TABLE_NAME+" WHERE "+AppContract.BlockedAppTable.COLUMN_PACKAGE_NAME+
                            " = \'"+data.packageName+"\'";
                    Cursor cursor = db.rawQuery(Query,null);

                    if(holder1.onOFF.isChecked()){
                        Log.e("BUTTON:","ON");
                        if(cursor.getCount()<1){
                            ContentValues contentValues = new ContentValues();
                            contentValues.put(AppContract.BlockedAppTable.COLUMN_APPNAME,data.appName);
                            contentValues.put(AppContract.BlockedAppTable.COLUMN_PACKAGE_NAME,data.packageName);

                            db.insert(AppContract.BlockedAppTable.TABLE_NAME,null,contentValues);
                        }

                     //   db_handle.PrintTable(AppContract.BlockedAppTable.TABLE_NAME);

                    }
                    else{
                        Log.e("BUTTON","Off");
                        if(cursor.getCount()<1){

                        }else{
                            String delQuery = " DELETE FROM "+AppContract.BlockedAppTable.TABLE_NAME+" WHERE "+AppContract.BlockedAppTable.COLUMN_PACKAGE_NAME+
                                    " = \'"+data.packageName+"\'";

                            db.execSQL(delQuery);
                           // db_handle.PrintTable(AppContract.BlockedAppTable.TABLE_NAME);
                        }
                    }

                    db.close();
                    db_handle.close();
                }
            });
    }

    @Override
    public int getItemCount() {
        return mList.size();
    }

    public List<String> getBlockedPackageList(){
        List<String>bList = new ArrayList<>();

        DBHelper dbHelper = new DBHelper(context);
        SQLiteDatabase db = dbHelper.getReadableDatabase();

        String rQuery = " SELECT * FROM "+ AppContract.BlockedAppTable.TABLE_NAME+" ";

        Cursor cursor = db.rawQuery(rQuery,null);

        while (cursor.moveToNext()){
            String packagename = cursor.getString(cursor.getColumnIndex(AppContract.BlockedAppTable.COLUMN_PACKAGE_NAME));
            bList.add(packagename);
        }

        cursor.close();
        db.close();

        dbHelper.PrintTable(AppContract.BlockedAppTable.TABLE_NAME);
        dbHelper.close();
        return bList;
    }

    public List<AppListData> setONitemFirst(List<AppListData> data){
        List<AppListData> d2 = new ArrayList<>();
        List<AppListData> d3 = new ArrayList<>(data);

        for( AppListData app : d3 ){
            if( this.bList.contains(app.packageName)){
                d2.add(app);
            }
        }



        d3.removeAll(d2);
        d2.addAll(d3);

        return d2;
    }

}
