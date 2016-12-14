package bounswe16group12.com.meanco.activities;

import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.support.v4.view.MenuItemCompat;
import android.support.v4.widget.SwipeRefreshLayout;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.text.Editable;
import android.text.TextUtils;
import android.text.TextWatcher;
import android.util.Log;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.SearchView;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import com.github.clans.fab.FloatingActionButton;

import java.util.ArrayList;
import java.util.List;

import bounswe16group12.com.meanco.MeancoApplication;
import bounswe16group12.com.meanco.R;
import bounswe16group12.com.meanco.database.DatabaseHelper;
import bounswe16group12.com.meanco.fragments.home.HomeActivityFragment;
import bounswe16group12.com.meanco.objects.Relation;
import bounswe16group12.com.meanco.objects.Tag;
import bounswe16group12.com.meanco.objects.Topic;
import bounswe16group12.com.meanco.tasks.PostRelation;


public class HomeActivity extends AppCompatActivity implements SearchView.OnQueryTextListener{
    static ArrayList<Tag> tagsOfTopic; //tags that are bound to topics
    SearchView searchView;
    private Spinner topicFromSpinner, topicToSpinner;

    //Home activity has search functionality, so changing the default menu is needed.
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.menu_search, menu);


        MenuItem searchItem = menu.findItem(R.id.search);
        searchView = (SearchView) MenuItemCompat.getActionView(searchItem);
        if (searchView != null) {
            searchView.setOnQueryTextListener(this);
            searchView.setIconifiedByDefault(false);
            searchView.setQueryHint("Search topic...");

        }

        MenuItemCompat.setOnActionExpandListener(searchItem, new MenuItemCompat.OnActionExpandListener() {
            @Override
            public boolean onMenuItemActionCollapse(MenuItem item) {
                searchView.clearFocus(); //to close soft keyboard when collapsed
                return true;  // Return true to collapse action view
            }

            @Override
            public boolean onMenuItemActionExpand(MenuItem item) {return true;}
        });

        return super.onCreateOptionsMenu(menu);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);

        getSupportActionBar().setDisplayShowHomeEnabled(true);
        getSupportActionBar().setIcon(R.drawable.rsz_meanco_logo);
        setTitle("  Meanco");

        //Add relation floating action button
        final FloatingActionButton relation_fab = (FloatingActionButton) findViewById(R.id.add_relation);
        relation_fab.setOnClickListener(
                new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        tagsOfTopic = new ArrayList<>();
                        final View customView = getLayoutInflater().inflate(R.layout.edit_relation, null, false);
                        final EditText relationNameEdit = (EditText) customView.findViewById(R.id.relation_name);
                        final CheckBox bidirectionalEdit = (CheckBox) customView.findViewById(R.id.bidirectional);

                        //Open alert dialog when button is pressed.
                        final AlertDialog dialog = new AlertDialog.Builder(HomeActivity.this)
                                .setTitle("Add relation")
                                .setView(customView)
                                .setPositiveButton("Next", new DialogInterface.OnClickListener() {
                                    public void onClick(DialogInterface dialog, int which) {

                                        String relationName = relationNameEdit.getText().toString();
                                        boolean isBidirectional = bidirectionalEdit.isChecked();

                                        Intent i = new Intent(HomeActivity.this, TopicSearchActivity.class);
                                        i.putExtra("relationName", relationName);
                                        i.putExtra("isBidirectional", isBidirectional);
                                        i.putExtra("fromOrTo", "from");
                                        startActivity(i);



                                    }
                                })
                                .setNegativeButton("Cancel", new DialogInterface.OnClickListener() {
                                    public void onClick(DialogInterface dialog, int which) {}
                                }).show();

                    }

                }
        );

        //ADD TOPIC

        final FloatingActionButton topic_fab = (FloatingActionButton) findViewById(R.id.add_topic);
        topic_fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                EditText temp = new EditText(HomeActivity.this);
                temp.setHint("Enter topic name");
                final EditText topicNameInput = temp;


                //TODO: next goes to intent
                new AlertDialog.Builder(HomeActivity.this)
                        .setTitle("Add topic")
                        .setView(topicNameInput)
                        .setPositiveButton("Next", new DialogInterface.OnClickListener() {
                            public void onClick(DialogInterface dialog, int which) {

                                String topicName = topicNameInput.getText().toString();

                                Intent i = new Intent(HomeActivity.this, TagSearchActivity.class);
                                i.putExtra("topicName", topicName);
                                i.putExtra("ifDetail", "false");
                                startActivity(i);
                            }
                        })
                        .setNegativeButton("Cancel", new DialogInterface.OnClickListener() {
                            public void onClick(DialogInterface dialog, int which) {

                            }
                        })
                        .show();


            }

        });

    }

    @Override
    public boolean onQueryTextSubmit(String query) {
        searchView.clearFocus();
        return true;
    }

    @Override
    public boolean onQueryTextChange(String newText) {
        if (TextUtils.isEmpty(newText)) {
            HomeActivityFragment.adapter.getFilter().filter("");
            HomeActivityFragment.listView.clearTextFilter();

        } else {
            HomeActivityFragment.adapter.getFilter().filter(newText.toString());


        }
        return true;
    }





}
