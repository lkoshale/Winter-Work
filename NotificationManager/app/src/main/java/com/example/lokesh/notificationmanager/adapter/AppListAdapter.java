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

import java.util.List;

/**
 * Created by lokesh on 24/12/17.
 */

public class AppListAdapter extends RecyclerView.Adapter<AppListAdapter.ViewHolder> {

    private List<AppListData> mList;
    private Context context;


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
        this.mList = mList;
        this.context = context;
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

                        db_handle.PrintTable(AppContract.BlockedAppTable.TABLE_NAME);

                    }
                    else{
                        Log.e("BUTTON","Off");
                        if(cursor.getCount()<1){

                        }else{
                            String delQuery = " DELETE FROM "+AppContract.BlockedAppTable.TABLE_NAME+" WHERE "+AppContract.BlockedAppTable.COLUMN_PACKAGE_NAME+
                                    " = \'"+data.packageName+"\'";

                            db.execSQL(delQuery);
                            db_handle.PrintTable(AppContract.BlockedAppTable.TABLE_NAME);
                        }
                    }

                }
            });
    }

    @Override
    public int getItemCount() {
        return mList.size();
    }



}
